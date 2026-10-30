using UnityEngine;

namespace WitheringRoomsArchipelago
{
    internal static class DeathLinkOverlay
    {
        private static string message = "";
        private static float hideAt = -1f;

        public static void Show(
            string text,
            float duration = 3.5f)
        {
            if (string.IsNullOrWhiteSpace(text))
                return;

            message = text;
            hideAt =
                Time.realtimeSinceStartup +
                Mathf.Max(0.5f, duration);

            Plugin.LogSource.LogInfo(
                $"[AP DEATHLINK UI] {text.Replace("\n", " / ")}"
            );
        }

        public static void OnGUI()
        {
            if (string.IsNullOrEmpty(message))
                return;

            if (Time.realtimeSinceStartup >= hideAt)
            {
                message = "";
                return;
            }

            GUIStyle style =
                new GUIStyle(GUI.skin.box);

            style.alignment =
                TextAnchor.MiddleCenter;

            style.fontSize = 20;
            style.wordWrap = true;

            float width =
                Mathf.Min(
                    640f,
                    Screen.width - 40f
                );

            float height =
                message.Contains("\n")
                    ? 72f
                    : 48f;

            Rect rect =
                new Rect(
                    (Screen.width - width) * 0.5f,
                    60f,
                    width,
                    height
                );

            GUI.Box(
                rect,
                message,
                style
            );
        }

        public static void Clear()
        {
            message = "";
            hideAt = -1f;
        }
    }
}