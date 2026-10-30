using UnityEngine;

namespace WitheringRoomsArchipelago
{
    internal static class DeathLinkNoticeUI
    {
        private static string currentMessage = "";
        private static float hideAtUnscaledTime = 0f;

        private static GUIStyle? labelStyle;
        private static Texture2D? backgroundTexture;

        public static void Show(string message, float durationSeconds = 2.75f)
        {
            if (string.IsNullOrWhiteSpace(message))
                return;

            currentMessage = message;
            hideAtUnscaledTime = Time.unscaledTime + Mathf.Max(0.25f, durationSeconds);

            Plugin.LogSource.LogInfo(
                $"[AP DEATHLINK UI] {message}"
            );
        }

        public static void OnGUI()
        {
            if (string.IsNullOrWhiteSpace(currentMessage))
                return;

            if (Time.unscaledTime >= hideAtUnscaledTime)
            {
                currentMessage = "";
                return;
            }

            EnsureGuiResources();

            float width =
                Mathf.Min(Screen.width * 0.72f, 900f);

            float height =
                Mathf.Clamp(Screen.height * 0.11f, 90f, 150f);

            float x =
                (Screen.width - width) * 0.5f;

            float y =
                Screen.height * 0.14f;

            Rect panelRect =
                new Rect(x, y, width, height);

            Color oldColor = GUI.color;

            GUI.color = new Color(0f, 0f, 0f, 0.78f);
            GUI.DrawTexture(panelRect, backgroundTexture!);

            GUI.color = Color.white;
            GUI.Label(panelRect, currentMessage, labelStyle!);

            GUI.color = oldColor;
        }

        private static void EnsureGuiResources()
        {
            if (backgroundTexture == null)
            {
                backgroundTexture = new Texture2D(1, 1, TextureFormat.RGBA32, false);
                backgroundTexture.SetPixel(0, 0, Color.white);
                backgroundTexture.Apply();
            }

            if (labelStyle == null)
            {
                labelStyle = new GUIStyle(GUI.skin.label);
                labelStyle.alignment = TextAnchor.MiddleCenter;
                labelStyle.wordWrap = true;
                labelStyle.richText = true;
                labelStyle.fontSize =
                    Mathf.RoundToInt(
                        Mathf.Clamp(Screen.height * 0.032f, 24f, 40f)
                    );
                labelStyle.fontStyle = FontStyle.Bold;
                labelStyle.normal.textColor = Color.white;
            }
        }
    }
}