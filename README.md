# candidate
Interview Monitor
A macOS application designed to detect overlay usage and unauthorized screen modifications during interviews and examinations to prevent cheating.
Overview
Interview Monitor is a third-party security application that monitors screen overlays and unauthorized applications during online interviews or examinations. The application runs as a background service to detect potential cheating attempts through screen overlays, unauthorized window manipulations, and suspicious application behavior.
Features
Core Functionality
    •    Overlay Detection: Real-time monitoring of screen overlays and unauthorized window layering
    •    Application Monitoring: Detection of suspicious applications running during interviews
    •    Screen Integrity Verification: Ensures screen content authenticity and detects modifications
    •    Background Operation: Runs silently without interfering with legitimate interview processes
    •    Security Reporting: Generates detailed reports of detected anomalies
Security Measures
    •    Detects unauthorized screen overlays
    •    Monitors window manipulation attempts
    •    Identifies suspicious application launches
    •    Tracks screen recording and screenshot attempts
    •    Validates screen content integrity
Requirements
System Requirements
    •    macOS: 10.15 (Catalina) or later
    •    Xcode: 12.0 or later for building from source
    •    Swift: 5.3 or later
    •    Memory: 100MB RAM minimum
    •    Disk Space: 50MB available storage
Permissions Required
    •    Screen Recording: Required for overlay detection
    •    Accessibility: Needed for window monitoring
    •    Privacy: Application monitoring permissions
Project Structure

mymonitor/
├── main.py
├── setup.py
├── README.md
├── screenshot_detector.py
├── pid_detector.py
├── copy_paste_detector.py
└── screen_monitor_detector.py

Security Considerations
Privacy Protection
    •    All monitoring data is processed locally
    •    No sensitive information is transmitted without consent
    •    Temporary data is securely disposed after use
    •    User privacy is maintained throughout the process
Compliance
    •    Designed to comply with educational testing standards
    •    Supports FERPA and privacy regulations
    •    Audit trail capabilities for compliance reporting
Troubleshooting
Common Issues
Permission Denied Errors
    •    Ensure Screen Recording permission is granted
    •    Check Accessibility permissions in System Preferences
    •    Restart the application after granting permissions
Overlay Detection Not Working
    •    Verify macOS version compatibility
    •    Check for conflicting security software
    •    Ensure proper code signing certificates
Performance Issues
    •    Monitor CPU and memory usage
    •    Adjust detection sensitivity settings
    •    Close unnecessary background applications
License
This project is licensed under the MIT License - see the LICENSE file for details.
Support
For technical support and questions:
    •    Create an issue in the GitHub repository
    •    Contact the development team
    •    Review the troubleshooting section above
Disclaimer
This application is designed for legitimate security monitoring purposes during interviews and examinations. Users must ensure compliance with applicable laws and regulations in their jurisdiction. The developers are not responsible for misuse of this software.