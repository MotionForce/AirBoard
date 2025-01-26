<script>
    import Tutorial from "$lib/components/Tutorial.svelte";

    function scrollToTutorial() {
        document.getElementById("tutorial").scrollIntoView({behavior: "smooth"});
    }
</script>

<div class="flex flex-col space-y-2 p-10 py-64 items-center align-middle bg-[#9CADBC]">
    <h1 class="text-9xl tracking-wide">AirBoard</h1>
    <p class="text-2xl">A keyboard. Without the keys. Or the board.</p>
    <button class="border-2 rounded-md p-2 bg-white" onclick={scrollToTutorial}>Start typing!</button>
</div>

<!--<div id="tutorial" class="bg-[#9CADBC] p-24 h-screen flex align-middle">-->
<div id="tutorial" class="bg-[#394955] p-24 h-screen flex align-middle">
    <Tutorial/>
</div>