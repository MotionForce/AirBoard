<script lang="ts">
    const idToMap = {
        // Fifth row (spacebar row)
        "rect88": "space",   // Space

        // Fourth row (ZXCV...)
        "rect82": "/",
        "rect81": ".",
        "rect80": ",",
        "rect79": "m",
        "rect78": "n",
        "rect77": "b",
        "rect76": "v",
        "rect75": "c",
        "rect74": "x",
        "rect73": "z",
        "rect84": "shift",   // Shift

        // Third row (ASDF...)
        "rect71": "'",
        "rect70": ";",
        "rect69": "l",
        "rect68": "k",
        "rect67": "j",
        "rect66": "h",
        "rect65": "g",
        "rect64": "f",
        "rect63": "d",
        "rect62": "s",
        "rect61": "a",
        "rect60": "⇪",   // Caps Lock

        // Second row (QWERTY...)
        "rect59": "]",
        "rect58": "[",
        "rect57": "p",
        "rect56": "o",
        "rect55": "i",
        "rect54": "u",
        "rect53": "y",
        "rect52": "t",
        "rect51": "r",
        "rect50": "e",
        "rect49": "w",
        "rect48": "q",
        "rect47": "\t",   // Tab

        // First row (numbers/symbols)
        "rect46": "🔇",  // Mute
        "rect45": "🌐",  // Language key
        "rect44": "⌫",  // Backspace
        "rect43": "=",
        "rect42": "-",
        "rect41": "0",
        "rect40": "9",
        "rect39": "8",
        "rect38": "7",
        "rect37": "6",
        "rect36": "5",
        "rect35": "4",
        "rect34": "3",
        "rect33": "2",
        "rect32": "1"
    }

    let {color, targetId, targetColor} = $props();
</script>

<div class="drop-shadow-lg h-full">
    <svg
            width="122.81421mm"
            height="41.480019mm"
            viewBox="0 0 122.81421 41.480019"
            version="1.1"
            id="svg1"
            xml:space="preserve"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:svg="http://www.w3.org/2000/svg">
        <g transform="translate(-9.1907662,-98.609175)">
            <g transform="matrix(0.20333342,0,0,0.20333342,1.7638103,78.542195)">
                <g stroke={color} fill="none" id="g106">
                    <g stroke-width="4" id="g59">
                        <!-- Render all rectangles except the selected one -->
                        {#each [
                            {id: 'rect32', x: 38.526001, y: 100.69},
                            {id: 'rect33', x: 78.526001, y: 100.69},
                            {id: 'rect34', x: 118.53, y: 100.69},
                            {id: 'rect35', x: 158.53, y: 100.69},
                            {id: 'rect36', x: 198.53, y: 100.69},
                            {id: 'rect37', x: 238.53, y: 100.69},
                            {id: 'rect38', x: 278.53, y: 100.69},
                            {id: 'rect39', x: 318.53, y: 100.69},
                            {id: 'rect40', x: 358.53, y: 100.69},
                            {id: 'rect41', x: 398.53, y: 100.69},
                            {id: 'rect42', x: 438.53, y: 100.69},
                            {id: 'rect43', x: 478.53, y: 100.69},
                            {id: 'rect44', x: 518.53003, y: 100.69},
                            {id: 'rect45', x: 558.53003, y: 100.69},
                            {id: 'rect46', x: 598.53003, y: 100.69},
                            {id: 'rect47', x: 38.526001, y: 140.69, width: 60},
                            {id: 'rect48', x: 98.526001, y: 140.69},
                            {id: 'rect49', x: 138.53, y: 140.69},
                            {id: 'rect50', x: 178.53, y: 140.69},
                            {id: 'rect51', x: 218.53, y: 140.69},
                            {id: 'rect52', x: 258.53, y: 140.69},
                            {id: 'rect53', x: 298.53, y: 140.69},
                            {id: 'rect54', x: 338.53, y: 140.69},
                            {id: 'rect55', x: 378.53, y: 140.69},
                            {id: 'rect56', x: 418.53, y: 140.69},
                            {id: 'rect57', x: 458.53, y: 140.69},
                            {id: 'rect58', x: 498.53, y: 140.69},
                            {id: 'rect59', x: 538.53003, y: 140.69},
                            {id: 'rect60', x: 38.526001, y: 180.69, width: 60},
                            {id: 'rect61', x: 118.53, y: 180.69},
                            {id: 'rect62', x: 158.53, y: 180.69},
                            {id: 'rect63', x: 198.53, y: 180.69},
                            {id: 'rect64', x: 238.53, y: 180.69},
                            {id: 'rect65', x: 278.53, y: 180.69},
                            {id: 'rect66', x: 318.53, y: 180.69},
                            {id: 'rect67', x: 358.53, y: 180.69},
                            {id: 'rect68', x: 398.53, y: 180.69},
                            {id: 'rect69', x: 438.53, y: 180.69},
                            {id: 'rect70', x: 478.53, y: 180.69},
                            {id: 'rect71', x: 518.53003, y: 180.69},
                            {id: 'rect72', x: 98.526001, y: 180.69, width: 20},
                            {id: 'rect73', x: 138.53, y: 220.69},
                            {id: 'rect74', x: 178.53, y: 220.69},
                            {id: 'rect75', x: 218.53, y: 220.69},
                            {id: 'rect76', x: 258.53, y: 220.69},
                            {id: 'rect77', x: 298.53, y: 220.69},
                            {id: 'rect78', x: 338.53, y: 220.69},
                            {id: 'rect79', x: 378.53, y: 220.69},
                            {id: 'rect80', x: 418.53, y: 220.69},
                            {id: 'rect81', x: 458.53, y: 220.69},
                            {id: 'rect82', x: 498.53, y: 220.69},
                            {id: 'rect83', x: 538.53003, y: 220.69, width: 100},
                            {id: 'rect84', x: 38.526001, y: 220.69, width: 100},
                            {id: 'rect85', x: 38.526001, y: 260.69},
                            {id: 'rect86', x: 78.526001, y: 260.69, width: 60},
                            {id: 'rect87', x: 138.53, y: 260.69, width: 60},
                            {id: 'rect88', x: 198.53, y: 260.69, width: 240},
                            {id: 'rect89', x: 438.53, y: 260.69, width: 60},
                            {id: 'rect90', x: 498.53, y: 260.69, width: 60},
                            {id: 'rect91', x: 558.53003, y: 260.69},
                            {id: 'rect92', x: 598.53003, y: 260.69}
                        ] as rect}
                            {#if rect.id !== targetId}
                                <rect
                                        height="40"
                                        width={rect.width || 40}
                                        y={rect.y}
                                        x={rect.x}
                                        id={rect.id}
                                        stroke={color}
                                        stroke-width="2"
                                />
                                <text
                                        x={rect.x + 20}
                                        y={rect.y + 25}
                                        font-size="15"
                                        fill={color}
                                        text-anchor="middle"
                                        style="!important;font-family: 'Roboto Slab'; font-weight: lighter;"
                                >
                                    {idToMap[rect.id]}
                                </text>
                            {/if}
                        {/each}
                        {#if targetId !== "path59"}
                            <path xmlns="http://www.w3.org/2000/svg"
                                  stroke={color}
                                  d="m 1003.4,220.18 v 71.2 h -35.56 v 71.21 h 142.36 v -71.21 -71.2 z"
                                  stroke-width="3.57025" id="path59" transform="matrix(0.56176,0,0,0.56176,14.838,17)"/>
                            {:else}
                            <path xmlns="http://www.w3.org/2000/svg"
                                  stroke={targetColor}
                                  d="m 1003.4,220.18 v 71.2 h -35.56 v 71.21 h 142.36 v -71.21 -71.2 z"
                                  stroke-width="3.57025" id="path59" transform="matrix(0.56176,0,0,0.56176,14.838,17)"/>
                        {/if}

                        <!-- Render the selected rectangle last -->
                        {#each [
                            {id: 'rect32', x: 38.526001, y: 100.69},
                            {id: 'rect33', x: 78.526001, y: 100.69},
                            {id: 'rect34', x: 118.53, y: 100.69},
                            {id: 'rect35', x: 158.53, y: 100.69},
                            {id: 'rect36', x: 198.53, y: 100.69},
                            {id: 'rect37', x: 238.53, y: 100.69},
                            {id: 'rect38', x: 278.53, y: 100.69},
                            {id: 'rect39', x: 318.53, y: 100.69},
                            {id: 'rect40', x: 358.53, y: 100.69},
                            {id: 'rect41', x: 398.53, y: 100.69},
                            {id: 'rect42', x: 438.53, y: 100.69},
                            {id: 'rect43', x: 478.53, y: 100.69},
                            {id: 'rect44', x: 518.53003, y: 100.69},
                            {id: 'rect45', x: 558.53003, y: 100.69},
                            {id: 'rect46', x: 598.53003, y: 100.69},
                            {id: 'rect47', x: 38.526001, y: 140.69, width: 60},
                            {id: 'rect48', x: 98.526001, y: 140.69},
                            {id: 'rect49', x: 138.53, y: 140.69},
                            {id: 'rect50', x: 178.53, y: 140.69},
                            {id: 'rect51', x: 218.53, y: 140.69},
                            {id: 'rect52', x: 258.53, y: 140.69},
                            {id: 'rect53', x: 298.53, y: 140.69},
                            {id: 'rect54', x: 338.53, y: 140.69},
                            {id: 'rect55', x: 378.53, y: 140.69},
                            {id: 'rect56', x: 418.53, y: 140.69},
                            {id: 'rect57', x: 458.53, y: 140.69},
                            {id: 'rect58', x: 498.53, y: 140.69},
                            {id: 'rect59', x: 538.53003, y: 140.69},
                            {id: 'rect60', x: 38.526001, y: 180.69, width: 60},
                            {id: 'rect61', x: 118.53, y: 180.69},
                            {id: 'rect62', x: 158.53, y: 180.69},
                            {id: 'rect63', x: 198.53, y: 180.69},
                            {id: 'rect64', x: 238.53, y: 180.69},
                            {id: 'rect65', x: 278.53, y: 180.69},
                            {id: 'rect66', x: 318.53, y: 180.69},
                            {id: 'rect67', x: 358.53, y: 180.69},
                            {id: 'rect68', x: 398.53, y: 180.69},
                            {id: 'rect69', x: 438.53, y: 180.69},
                            {id: 'rect70', x: 478.53, y: 180.69},
                            {id: 'rect71', x: 518.53003, y: 180.69},
                            {id: 'rect72', x: 98.526001, y: 180.69, width: 20},
                            {id: 'rect73', x: 138.53, y: 220.69},
                            {id: 'rect74', x: 178.53, y: 220.69},
                            {id: 'rect75', x: 218.53, y: 220.69},
                            {id: 'rect76', x: 258.53, y: 220.69},
                            {id: 'rect77', x: 298.53, y: 220.69},
                            {id: 'rect78', x: 338.53, y: 220.69},
                            {id: 'rect79', x: 378.53, y: 220.69},
                            {id: 'rect80', x: 418.53, y: 220.69},
                            {id: 'rect81', x: 458.53, y: 220.69},
                            {id: 'rect82', x: 498.53, y: 220.69},
                            {id: 'rect83', x: 538.53003, y: 220.69, width: 100},
                            {id: 'rect84', x: 38.526001, y: 220.69, width: 100},
                            {id: 'rect85', x: 38.526001, y: 260.69},
                            {id: 'rect86', x: 78.526001, y: 260.69, width: 60},
                            {id: 'rect87', x: 138.53, y: 260.69, width: 60},
                            {id: 'rect88', x: 198.53, y: 260.69, width: 240},
                            {id: 'rect89', x: 438.53, y: 260.69, width: 60},
                            {id: 'rect90', x: 498.53, y: 260.69, width: 60},
                            {id: 'rect91', x: 558.53003, y: 260.69},
                            {id: 'rect92', x: 598.53003, y: 260.69}
                        ] as rect}
                            {#if rect.id === targetId}
                                <rect
                                        height="40"
                                        width={rect.width || 40}
                                        y={rect.y}
                                        x={rect.x}
                                        id={rect.id}
                                        stroke={targetColor}
                                        fill={targetColor}
                                        stroke-width="2"
                                />
                                <text
                                        x={rect.x + 20}
                                        y={rect.y + 25}
                                        font-size="15"
                                        fill={color}
                                        text-anchor="middle"
                                        style="font-family: 'Roboto Slab'; font-weight: lighter;"
                                >
                                {idToMap[rect.id]}
                                </text>
                            {/if}
                        {/each}
                    </g>
                </g>
            </g>
        </g>
    </svg>
</div>