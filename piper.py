import tkinter as tk
from tkinter import ttk, filedialog
import yt_dlp as youtube_dl
import threading
import queue
import os


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Piper — YouTube Downloader")
    root.geometry("480x520")
    root.resizable(False, False)

    # Set a futuristic dark theme with neon highlights
    root.configure(bg="#181A20")

    style = ttk.Style()
    style.theme_use('clam')

    # Futuristic colors
    bg_color = "#181A20"
    frame_color = "#23263A"
    accent_color = "#00FFF7"   # Neon cyan
    accent2_color = "#A259FF"  # Neon purple
    text_color = "#E0E0E0"

    # Detect whether the Orbitron font is available and use it for the title
    try:
        import tkinter.font as tkfont
        title_font = ("Orbitron", 18, "bold") if "Orbitron" in tkfont.families() else ("Segoe UI", 18, "bold")
    except Exception:
        title_font = ("Segoe UI", 18, "bold")

    style.configure("TFrame", background=frame_color)
    style.configure("TLabel", background=frame_color, foreground=text_color, font=("Segoe UI", 10))
    style.configure("Title.TLabel", background=bg_color, foreground=accent_color, font=title_font)
    style.configure("TButton", background=accent_color, foreground=bg_color,
                    font=("Segoe UI", 10, "bold"), borderwidth=0,
                    focusthickness=3, focuscolor=accent2_color)
    style.map("TButton",
              background=[('active', accent2_color), ('pressed', accent_color)],
              foreground=[('active', text_color), ('pressed', bg_color)])
    style.configure("TRadiobutton", background=frame_color, foreground=accent2_color,
                    font=("Segoe UI", 10, "bold"))
    style.map("TRadiobutton",
              background=[('selected', accent_color)],
              foreground=[('selected', bg_color)])
    style.configure("TProgressbar", background=accent_color, troughcolor=frame_color,
                    bordercolor=accent2_color, lightcolor=accent_color,
                    darkcolor=accent2_color, thickness=12)

    # ── Layout ──────────────────────────────────────────────────────────────

    # Create a frame for input elements
    input_frame = ttk.Frame(root, style="TFrame")
    input_frame.pack(pady=16, fill=tk.X, padx=20)

    # Title label
    title_label = ttk.Label(input_frame, text="Piper", style="Title.TLabel")
    title_label.pack(pady=10)

    # URL input
    url_label = ttk.Label(input_frame, text="Enter YouTube URL:", style="TLabel")
    url_label.pack()
    url_entry = tk.Entry(
        input_frame, width=50, font=("Consolas", 10),
        bg=frame_color, fg=accent_color, insertbackground=accent_color,
        relief=tk.FLAT, highlightthickness=1, highlightbackground=accent2_color,
    )
    url_entry.pack(pady=5)

    # Format selection
    type_label = ttk.Label(input_frame, text="Select type:", style="TLabel")
    type_label.pack()
    type_var = tk.StringVar(value="video")
    video_radio = ttk.Radiobutton(input_frame, text="Video (1080p)",
                                  variable=type_var, value="video",
                                  style="TRadiobutton")
    audio_radio = ttk.Radiobutton(input_frame, text="Audio (High Quality MP3)",
                                  variable=type_var, value="audio",
                                  style="TRadiobutton")
    video_radio.pack()
    audio_radio.pack()

    # Download directory row
    download_dir_var = tk.StringVar(value=os.path.expanduser('~/Downloads'))

    dir_frame = ttk.Frame(root, style="TFrame")
    dir_frame.pack(fill=tk.X, padx=20, pady=(0, 6))

    save_label = ttk.Label(dir_frame, textvariable=download_dir_var, style="TLabel",
                           wraplength=340, anchor="w")
    save_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

    def browse_dir():
        chosen = filedialog.askdirectory(initialdir=download_dir_var.get())
        if chosen:
            download_dir_var.set(chosen)

    browse_button = ttk.Button(dir_frame, text="Browse…", command=browse_dir, style="TButton")
    browse_button.pack(side=tk.RIGHT)

    # Download button
    download_button = ttk.Button(root, text="Download", style="TButton")
    download_button.pack(pady=10)

    # Progress bar + status log
    progress_frame = ttk.Frame(root, style="TFrame")
    progress_frame.pack(pady=(0, 14), padx=20, fill=tk.X)

    progress = ttk.Progressbar(progress_frame, orient='horizontal',
                               mode='determinate', length=440, style="TProgressbar")
    progress.pack(pady=(0, 7), fill=tk.X)
    progress['maximum'] = 100
    progress['value'] = 0

    status_text = tk.Text(
        progress_frame, height=6, width=50,
        bg=frame_color, fg=accent_color, insertbackground=accent2_color,
        font=("Consolas", 10), borderwidth=0,
        highlightthickness=1, highlightbackground=accent2_color,
        state=tk.DISABLED,
    )
    status_text.pack(pady=5, fill=tk.X)

    # ── Logic ────────────────────────────────────────────────────────────────

    status_queue = queue.Queue()

    def progress_hook(d):
        if d.get('status') == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            # Guard against division by zero when total is unknown or zero
            total = max(d.get('total_bytes') or d.get('total_bytes_estimate') or 1, 1)
            pct = downloaded / total * 100
            status_queue.put(('text', f"Downloading… {pct:.1f}%\n"))
            status_queue.put(('bar', pct))
        elif d.get('status') == 'finished':
            status_queue.put(('text', "Download finished; post-processing…\n"))
            status_queue.put(('bar', 100))

    def download_thread(url, download_type, save_dir):
        """Background worker — receives all needed data as arguments to avoid
        accessing Tkinter widgets from outside the main thread."""
        if download_type == "video":
            ydl_opts = {
                'format': 'bestvideo[height<=1080]+bestaudio/bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'progress_hooks': [progress_hook],
                'outtmpl': os.path.join(save_dir, '%(title)s-%(id)s-video.%(ext)s'),
            }
        else:
            ydl_opts = {
                'format': 'bestaudio/best',
                'progress_hooks': [progress_hook],
                'outtmpl': os.path.join(save_dir, '%(title)s-%(id)s-audio.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            status_queue.put(('text', f"Error: {e}\n"))
        finally:
            status_queue.put(('enable_button', None))

    def download():
        url = url_entry.get().strip()
        if not url:
            status_text.config(state=tk.NORMAL)
            status_text.insert(tk.END, "Please enter a URL.\n")
            status_text.config(state=tk.DISABLED)
            return
        # Capture widget values in the main thread before spawning worker
        download_type = type_var.get()
        save_dir = download_dir_var.get()

        download_button.config(state=tk.DISABLED)
        progress['value'] = 0
        status_text.config(state=tk.NORMAL)
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, "Starting download…\n")
        status_text.config(state=tk.DISABLED)

        thread = threading.Thread(
            target=download_thread,
            args=(url, download_type, save_dir),
            daemon=True,
        )
        thread.start()

    download_button.config(command=download)

    def check_queue():
        while not status_queue.empty():
            msg = status_queue.get()
            if isinstance(msg, tuple):
                msg_type, data = msg
                if msg_type == 'text':
                    status_text.config(state=tk.NORMAL)
                    status_text.insert(tk.END, data)
                    status_text.see(tk.END)
                    status_text.config(state=tk.DISABLED)
                elif msg_type == 'bar':
                    progress['value'] = data
                elif msg_type == 'enable_button':
                    download_button.config(state=tk.NORMAL)
                    progress['value'] = 0
        root.after(100, check_queue)

    root.after(100, check_queue)
    root.mainloop()


if __name__ == "__main__":
    main()