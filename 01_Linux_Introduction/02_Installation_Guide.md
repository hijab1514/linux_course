# 🖥️ Linux Installation Guide (Virtual Machine Method)

This guide will walk you through installing Linux on a **Virtual Machine (VM)** so you can learn safely without affecting your main computer.

---

## 1️⃣ What is a Virtual Machine?
A **Virtual Machine (VM)** is software that lets you run another operating system inside your current system.  
Think of it as a **computer inside your computer**.

**Advantages of VMs:**
- Safe environment for testing and learning.
- Can run multiple OS side-by-side.
- Take **snapshots** to roll back changes.
- No risk to your main OS.

---

## 2️⃣ Tools You Will Need
| Tool | Description | Download Link |
|------|-------------|---------------|
| VirtualBox | Free and open-source VM software | [https://www.virtualbox.org](https://www.virtualbox.org) |
| Linux ISO | Installation image of a Linux distro | [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) |

---

## 3️⃣ Download & Install VirtualBox
1. Visit [VirtualBox Downloads](https://www.virtualbox.org/wiki/Downloads).
2. Select your OS (Windows, macOS, Linux).
3. Download and run the installer.
4. Follow the on-screen instructions (default settings are fine).

---

## 4️⃣ Download Linux ISO
For beginners, **Ubuntu LTS** is recommended:
- Go to [Ubuntu Downloads](https://ubuntu.com/download/desktop).
- Select **Long-Term Support (LTS)** version.
- Download the `.iso` file.

---

## 5️⃣ Create a Virtual Machine
1. **Open VirtualBox** and click `New`.
2. Enter:
   - Name: `Ubuntu` (or any name you prefer)
   - Type: `Linux`
   - Version: `Ubuntu (64-bit)`
3. Click `Next`.

---

## 6️⃣ Allocate Resources
- **Memory (RAM):** Minimum 2 GB (2048 MB), recommended 4 GB+.
- **CPU Cores:** At least 2 cores for better performance.

---

## 7️⃣ Create a Virtual Hard Disk
- Select **Create a virtual hard disk now**.
- Disk type: `VDI (VirtualBox Disk Image)`.
- Storage: `Dynamically allocated`.
- Size: **20 GB** minimum, **40 GB** recommended.

---

## 8️⃣ Attach Linux ISO
- Go to **Settings → Storage**.
- Under **Controller: IDE**, click **Empty**.
- Click the small disk icon → **Choose a disk file…**.
- Select the downloaded Ubuntu ISO.
- Click `OK`.

---

## 9️⃣ Start the Virtual Machine
- Click `Start` in VirtualBox.
- Ubuntu installation will begin.

---

## 🔟 Install Ubuntu
1. Select **Install Ubuntu**.
2. Choose **Keyboard Layout** → `Continue`.
3. **Installation Type:** Choose "Erase disk and install Ubuntu" (this affects only the VM, not your real PC).
4. Set **Timezone**.
5. Create a **Username** and **Password**.
6. Click `Install Now`.

---

## 1️⃣1️⃣ After Installation
- Remove ISO:
  - **Settings → Storage → Remove ISO**.
- Restart VM.
- Log in with your username and password.

---

## 1️⃣2️⃣ Taking Snapshots (Recommended)
Snapshots let you save your VM state:
- **Machine → Take Snapshot**.
- Name it: `Fresh Install`.
- You can revert to this point anytime.

---

## 📌 Pro Tips
- Keep your VM updated:  
  ```bash
  sudo apt update && sudo apt upgrade -y


Use full-screen mode in VirtualBox for a better experience (Host Key + F).

Install Guest Additions for better performance and shared clipboard.
