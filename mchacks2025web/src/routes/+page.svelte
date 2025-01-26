<script lang="ts">
    import Tutorial from "$lib/components/Tutorial.svelte";
    import HandGestureRecognition from './HandGestureRecognition.svelte';
    import KeyboardComponent from "$lib/components/KeyboardComponent.svelte";

    function scrollToTutorial() {
        document.getElementById("tutorial").scrollIntoView({behavior: "smooth"});
    }
</script>
<!--<KeyboardComponent/>-->

<div class="flex flex-col p-10 py-64 items-center align-middle bg-[#9CADBC]">
    <h1 class="text-9xl mb-2 typewriter w-fit">AirBoard</h1>
    <p class="text-2xl mb-7">A keyboard without the keys. Or the board.</p>
    <button class="border-2 border-cyan-700 rounded-full p-3 bg-cyan-100 saturate-50" onclick={scrollToTutorial}>Start typing!</button>
</div>
<main class="min-h-screen bg-gray-50">
    <HandGestureRecognition />
</main>


<!--<div id="tutorial" class="bg-[#9CADBC] p-24 h-screen flex align-middle">-->
<!--<div id="/tutorial" class="bg-[#394955] p-24 h-screen flex align-middle">-->
<!--    <Tutorial/>-->
<!--</div>-->

<style>
    .typewriter {
        overflow: hidden;
        border-right: .15em solid darkslategray;
        white-space: nowrap;
        letter-spacing: .1em;
        animation:
                typing 2s steps(10, end),
                blink-caret .75s step-end infinite;
    }

    /* The typing effect */
    @keyframes typing {
        from { width: 0 }
        to { width: 42% }
    }

    /* The typewriter cursor effect */
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: darkslategray; }
    }
</style>