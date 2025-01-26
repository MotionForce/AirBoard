<script>
    import Keyboard from "$lib/components/svg/Keyboard.svelte";
    import {onMount} from "svelte";

    const charToIdMap = {
        // First row (numbers/symbols)
        "1": "rect32",
        "2": "rect33",
        "3": "rect34",
        "4": "rect35",
        "5": "rect36",
        "6": "rect37",
        "7": "rect38",
        "8": "rect39",
        "9": "rect40",
        "0": "rect41",
        "-": "rect42",
        "=": "rect43",
        "⌫": "rect44",  // Backspace
        "🌐": "rect45",  // Language key
        "🔇": "rect46",  // Mute

        // Second row (QWERTY...)
        "\t": "rect47",   // Tab
        "q": "rect48",
        "w": "rect49",
        "e": "rect50",
        "r": "rect51",
        "t": "rect52",
        "y": "rect53",
        "u": "rect54",
        "i": "rect55",
        "o": "rect56",
        "p": "rect57",
        "[": "rect58",
        "]": "rect59",

        // Third row (ASDF...)
        "⇪": "rect60",   // Caps Lock
        "a": "rect61",
        "s": "rect62",
        "d": "rect63",
        "f": "rect64",
        "g": "rect65",
        "h": "rect66",
        "j": "rect67",
        "k": "rect68",
        "l": "rect69",
        ";": "rect70",
        "'": "rect71",
        "↵": "rect72",   // Enter

        // Fourth row (ZXCV...)
        "z": "rect73",
        "x": "rect74",
        "c": "rect75",
        "v": "rect76",
        "b": "rect77",
        "n": "rect78",
        "m": "rect79",
        ",": "rect80",
        ".": "rect81",
        "/": "rect82",
        "right_shift": "rect83",   // Right Shift

        // Fifth row (spacebar row)
        "space": "rect88",   // Space
    };

    let highlightColor = '#00ff00';


    let selectedId = $state();

    let text = $state("");

    function set_selected_id(char) {
        console.log(charToIdMap[char]);
        selectedId = charToIdMap[char];
    }
</script>

{text}
{selectedId}
<input type="text" id="selectedId" bind:value={text} oninput={() => set_selected_id(text)}>

<Keyboard color="white" targetId={selectedId} targetColor={highlightColor}/>