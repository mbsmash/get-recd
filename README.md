# Video Recorder

A single-page HTML app that lets you record gameplay or webcam footage directly to disk using the MediaStream Recording API and the File System Access API. It runs entirely client-side, so you can deploy it on GitHub Pages or any static host.

## Requirements

- **Secure context** – browsers require HTTPS (or `http://localhost`) for camera access and writable file handles. Opening `index.html` directly from disk will not work.
- **Supported browser** – Chrome, Edge, Arc, and other Chromium-based browsers that expose the File System Access API can stream recordings straight to the drive you pick. Brave, Firefox, and Safari currently block this API, so the "Choose Save Location" button will stay disabled.

To publish on GitHub Pages, push the repo to GitHub and enable Pages for the main branch. GitHub will host it over HTTPS automatically.

## Using the app

1. Open the page. The app will immediately request camera and microphone access so it can populate the dropdowns.
2. Pick your **video** and **audio** sources from the selectors if you have multiple devices. The preview refreshes automatically when you change either input.
3. Optional: choose a **resolution preference** (browser default, 1080p, or 720p). The status readout confirms the actual resolution delivered by your hardware/browser.
4. Click **Choose Save Location** to decide where the `.webm` file should be written. The app streams chunks directly to the selected file—nothing is buffered in memory or cached by the browser.
5. Hit **Start Recording** to capture video (and audio if available). Use **Stop Recording** to finish; the file closes automatically and is ready immediately.

## Common issues & troubleshooting

- **"Camera access requires HTTPS"** – serve the page from `https://` or `http://localhost`. GitHub Pages already uses HTTPS; local testing needs a dev server rather than opening the file directly.
- **"Choose Save Location" is disabled** – your browser doesn’t expose the File System Access API. Switch to Chrome/Edge/Arc, or (in Brave) enable the `#file-system-access-api` flag and restart the browser.
- **Permission errors** – make sure the site is allowed to use the camera/mic in both the browser UI (lock icon, permissions panel) and the OS privacy settings. Reload after changing permissions.
- **Device busy / NotReadableError** – close other apps that might be using the same capture device (Teams, Zoom, OBS, etc.) and try again.
- **Silent recordings** – if no microphones are detected the audio dropdown is disabled and the status bar warns that captures will be silent. Plug in a mic and click the refresh icon in the browser’s permission bar or reload the page.

If something goes wrong, check the status line under the buttons—it surfaces the exact error plus hints about how to resolve it.
