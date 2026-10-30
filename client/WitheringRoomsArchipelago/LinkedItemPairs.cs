using System;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// The five vanilla equipment relationships where acquiring the
    /// primary outfit automatically awards a second REAL randomized item.
    ///
    /// These are deliberately explicit.
    ///
    /// Do NOT generalize this to every implied/secondary item because
    /// Withering Rooms uses secondary awards heavily for hidden quest
    /// state and bookkeeping.
    /// </summary>
    internal static class LinkedItemPairs
    {
        private static readonly Dictionary<string, string>
            PrimaryToSecondary =
                new Dictionary<string, string>(
                    StringComparer.OrdinalIgnoreCase
                )
                {
                    {
                        // Dirty Initiate Dress -> Sack
                        "ca2ccd4d435e01c4394e1d526a207ba0",
                        "0b3ba885adefe464289c0ea2a127c1f5"
                    },

                    {
                        // Nurse Uniform -> Nurse's Hat
                        "ed18eac8bab2f9f4eb819515ec2fe5e0",
                        "d7098d1155e74c04b9294bd83862f96c"
                    },

                    {
                        // Starry Dress -> Starry Head Sack
                        "5f3ee41f0af26814cae3d67e55bb042a",
                        "a3cdae23298e71644850ac3715e15667"
                    },

                    {
                        // Merry Band Cloak -> Merry Band Mask
                        "e509548d1570e9840b07b358ba0053f6",
                        "75184a2b8abafe844981befe56840ffc"
                    },

                    {
                        // Initiate Dress -> Initiate Hat
                        "0a61e772e5e6b77488778ffaaada65f7",
                        "43dc9b2f464420f46ba40107e6668d09"
                    }
                };


        private static readonly Dictionary<string, string>
            PartnerByGuid =
                BuildPartnerMap();


        public static bool TryGetSecondaryForPrimary(
            string primaryGuid,
            out string secondaryGuid)
        {
            return PrimaryToSecondary.TryGetValue(
                primaryGuid,
                out secondaryGuid
            );
        }


        public static bool TryGetPartner(
            string guid,
            out string partnerGuid)
        {
            return PartnerByGuid.TryGetValue(
                guid,
                out partnerGuid
            );
        }


        private static Dictionary<string, string>
            BuildPartnerMap()
        {
            Dictionary<string, string> result =
                new Dictionary<string, string>(
                    StringComparer.OrdinalIgnoreCase
                );

            foreach (
                KeyValuePair<string, string> pair
                in PrimaryToSecondary)
            {
                result[pair.Key] =
                    pair.Value;

                result[pair.Value] =
                    pair.Key;
            }

            return result;
        }
    }
}