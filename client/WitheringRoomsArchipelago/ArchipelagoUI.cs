using System;
using UnityEngine;
using static DialogMerchantNode;

namespace WitheringRoomsArchipelago
{
    public class ArchipelagoUI
    {
        public static bool Visible = true;

        public static string ServerAddress = "";
        public static string SlotName = "";
        public static string Password = "";


        private string connectedAddress = "";
        private string connectedSlotName = "";
        private string connectedPassword = "";

        private bool connectionInProgress = false;
        private string connectionError = "";

        private bool FieldsMatchCurrentConnection
        {
            get
            {
                return ArchipelagoClient.Connected &&
                       ServerAddress.Trim() == connectedAddress &&
                       SlotName.Trim() == connectedSlotName &&
                       Password == connectedPassword;
            }
        }

        private Rect panelRect =
            new Rect(50, 50, 500, 330);

        private bool connectionSucceeded = false;
        private float successTimer = 0f;

        private const float SuccessHoldTime = 2.0f;
        private const float SuccessFadeTime = 1.0f;

        public void Start()
        {
            Plugin.LogSource.LogInfo(
                "[AP UI] Connection UI initialized."
            );

            Visible = true;

            Plugin.LogSource.LogInfo(
                "[AP UI] About to load saved connection."
            );

            bool loaded =
                ArchipelagoConnectionSettings.TryLoad(
                    out string address,
                    out string slotName,
                    out string password
                );

            Plugin.LogSource.LogInfo(
                $"[AP UI] Saved connection load result={loaded}"
            );

            if (loaded)
            {
                ServerAddress = address;
                SlotName = slotName;
                Password = password;

                Plugin.LogSource.LogInfo(
                    $"[AP UI] Loaded fields: " +
                    $"Server={ServerAddress}, Slot={SlotName}"
                );

                Plugin.LogSource.LogInfo(
                    "[AP UI] Attempting previous connection."
                );

                RequestConnection();
            }
        }

        public void Update()
        {
            if (Input.GetKeyDown(KeyCode.F7))
            {
                Visible = !Visible;

                // If the player manually reopens the window,
                // cancel any old success animation.
                if (Visible)
                {
                    connectionSucceeded = false;
                    successTimer = 0f;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP UI] Connection window visible={Visible}"
                );
            }

            if (connectionSucceeded && Visible)
            {
                successTimer += Time.unscaledDeltaTime;

                if (successTimer >=
                    SuccessHoldTime + SuccessFadeTime)
                {
                    Visible = false;
                    connectionSucceeded = false;
                    successTimer = 0f;

                    Plugin.LogSource.LogInfo(
                        "[AP UI] Connection window fade complete."
                    );
                }
            }
        }

        public void OnGUI()
        {
            if (!Visible)
                return;

            float alpha = 1.0f;

            if (connectionSucceeded &&
                successTimer > SuccessHoldTime)
            {
                float fadeProgress =
                    (successTimer - SuccessHoldTime)
                    / SuccessFadeTime;

                alpha = 1.0f -
                    Mathf.Clamp01(fadeProgress);
            }

            Color oldColor = GUI.color;

            GUI.color = new Color(
                oldColor.r,
                oldColor.g,
                oldColor.b,
                oldColor.a * alpha
            );

            DrawConnectionPanel();

            GUI.color = oldColor;
        }

        private void DrawConnectionPanel()
        {
            float x = panelRect.x;
            float y = panelRect.y;
            float width = panelRect.width;

            string oldServer = ServerAddress;
            string oldSlot = SlotName;
            string oldPassword = Password;

            GUI.Box(
                panelRect,
                "Withering Rooms Archipelago"
            );

            y += 45;

            GUI.Label(
                new Rect(x + 25, y, width - 50, 25),
                "Server Address"
            );

            y += 25;

            ServerAddress = GUI.TextField(
                new Rect(x + 25, y, width - 50, 30),
                ServerAddress
            );

            y += 45;

            GUI.Label(
                new Rect(x + 25, y, width - 50, 25),
                "Slot Name"
            );

            y += 25;

            SlotName = GUI.TextField(
                new Rect(x + 25, y, width - 50, 30),
                SlotName
            );

            y += 45;

            GUI.Label(
                new Rect(x + 25, y, width - 50, 25),
                "Password"
            );

            y += 25;

            Password = GUI.PasswordField(
                new Rect(x + 25, y, width - 50, 30),
                Password,
                '*'
            );

            y += 50;

            if (!connectionInProgress &&
                (ServerAddress != oldServer ||
                 SlotName != oldSlot ||
                 Password != oldPassword))
                        {
                            connectionError = "";
                        }

            if (connectionSucceeded)
            {
                GUIStyle successStyle =
                    new GUIStyle(GUI.skin.label);

                successStyle.alignment =
                    TextAnchor.MiddleCenter;

                successStyle.fontStyle =
                    FontStyle.Bold;

                successStyle.normal.textColor =
                    Color.green;

                GUI.Label(
                    new Rect(x + 25, y, width - 50, 35),
                    "Connection successful!",
                    successStyle
                );
            }
            else if (FieldsMatchCurrentConnection)
            {
                GUIStyle connectedStyle =
                    new GUIStyle(GUI.skin.label);

                connectedStyle.alignment =
                    TextAnchor.MiddleCenter;

                connectedStyle.fontStyle =
                    FontStyle.Bold;

                connectedStyle.normal.textColor =
                    Color.green;

                GUI.Label(
                    new Rect(x + 25, y, width - 50, 35),
                    "Connected",
                    connectedStyle
                );
            }
            else
            {
                if (connectionInProgress)
                {
                    bool oldEnabled = GUI.enabled;
                    GUI.enabled = false;

                    GUI.Button(
                        new Rect(x + 25, y, width - 50, 35),
                        "Connecting..."
                    );

                    GUI.enabled = oldEnabled;
                }
                else if (!string.IsNullOrEmpty(connectionError))
                {
                    GUIStyle errorStyle =
                        new GUIStyle(GUI.skin.label);

                    errorStyle.alignment =
                        TextAnchor.MiddleCenter;

                    errorStyle.fontStyle =
                        FontStyle.Bold;

                    errorStyle.normal.textColor =
                        Color.red;

                    GUI.Label(
                        new Rect(x + 25, y, width - 50, 35),
                        connectionError,
                        errorStyle
                    );

                    y += 40;

                    if (GUI.Button(
                        new Rect(x + 25, y, width - 50, 35),
                        "Try Again"
                    ))
                    {
                        RequestConnection();
                    }
                }
                else
                {
                    if (GUI.Button(
                        new Rect(x + 25, y, width - 50, 35),
                        ArchipelagoClient.Connected
                            ? "Reconnect"
                            : "Connect"
                    ))
                    {
                        RequestConnection();
                    }
                }
            }
        }

        private void RequestConnection()
        {
            // Prevent multiple simultaneous connection attempts.
            if (connectionInProgress)
                return;

            if (string.IsNullOrWhiteSpace(ServerAddress))
            {
                connectionError = "Server address is required";

                Plugin.LogSource.LogWarning(
                    "[AP UI] Server address is empty."
                );

                return;
            }

            if (string.IsNullOrWhiteSpace(SlotName))
            {
                connectionError = "Slot name is required";

                Plugin.LogSource.LogWarning(
                    "[AP UI] Slot name is empty."
                );

                return;
            }

            string address = ServerAddress.Trim();
            string slotName = SlotName.Trim();
            string password = Password;

            // Set UI state BEFORE starting the background task.
            connectionInProgress = true;
            connectionError = "";
            connectionSucceeded = false;
            successTimer = 0f;

            Plugin.LogSource.LogInfo(
                $"[AP UI] Attempting connection to {address} " +
                $"as slot \"{slotName}\"."
            );

            System.Threading.Tasks.Task.Run(() =>
            {
                bool success = ArchipelagoClient.ConnectSync(
                    address,
                    slotName,
                    "Withering Rooms",
                    password
                );

                connectionInProgress = false;

                if (success)
                {
                    connectedAddress = address;
                    connectedSlotName = slotName;
                    connectedPassword = password;

                    ArchipelagoConnectionSettings.Save(
                        address,
                        slotName,
                        password
                    );

                    connectionError = "";
                    connectionSucceeded = true;
                    successTimer = 0f;

                    Plugin.LogSource.LogInfo(
                        "[AP UI] Connection succeeded."
                    );
                }
                else
                {
                    connectionSucceeded = false;

                    connectionError =
                        string.IsNullOrEmpty(
                            ArchipelagoClient.LastConnectionError)
                        ? "Connection failed"
                        : ArchipelagoClient.LastConnectionError;

                    Plugin.LogSource.LogWarning(
                        $"[AP UI] Connection failed: " +
                        $"{connectionError}"
                    );
                }
            });
        }
    }
}