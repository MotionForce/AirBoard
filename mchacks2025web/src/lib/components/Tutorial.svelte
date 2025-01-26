<script lang="ts">
    import Keyboard from "$lib/components/svg/Keyboard.svelte";
    import Hand from "$lib/components/svg/Hand.svelte";
    import {onMount} from "svelte";
    import {fade} from "svelte/transition";
    import {messages, connectWebSocket, sendMessage} from "$lib/websocket";
    import {onMount} from "svelte";

    const required_keys = [
        "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"
    ];

    let current_key = $state(required_keys[0]);

    let loaded = $state(false);
    let handContainer: HTMLElement = $state(null);

    let tutorial_ended = $state(false);
    let setup_phase = $state(true);

    $effect(() => {
        if (tutorial_ended) {
            getStream();
        }
    });

    let video;
    let videoRef;

    async function getStream() {
        try {
            video = await navigator.mediaDevices.getUserMedia({
                video: true,
                audio: false
            });
            videoRef.srcObject = video;
        } catch (err) {
            console.error(err);
        }
        console.log(video.getTracks()[0])
    }

    onMount(() => {
        // Access webcam
        const video = document.getElementById('webcam');
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
                startFrameCapture();
            })
            .catch(err => console.error("Webcam error:", err));

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    loaded = true;
                } else {
                    loaded = false;
                }
            });
        });
        observer.observe(handContainer);
    });
</script>

{#if !tutorial_ended}
    <div transition:fade>
        <div class="p-4 py-8 border-2 rounded-3xl overflow-clip bg-gradient-to-tr from-blue-300  to-pink-300">
            <div>
                <Keyboard color="#394955"/>
            </div>
            {#if !setup_phase}
                <div class="absolute left-0 right-0 flex flex-col py-96 mb-[-37%] space-y-6 bottom-0 items-center justify-center align-middle">
                    <div class="rounded-2xl border-4 p-4 backdrop-blur-xl backdrop-brightness-[1.3] animate-title {!loaded ? 'pause' : ''}">
                        <h3 class="text-3xl">Place your fingers over the middle row, palms about 2cm in the air.</h3>
                    </div>
                    <div class="mt-3 animate-button {!loaded ? 'pause' : ''}">
                        <button class="border-2 p-4 text-xl rounded-md bg-white" onclick={() => setup_phase=true}>
                            Ready!
                        </button>
                        <div class="text-white drop-shadow-2xl flex flex-col items-center space-y-1 animate-arrow {!loaded ? 'pause' : ''}">
                            <img src="/svg/up-arrow-svgrepo-com.svg" alt="up arrow" width="32" class="invert">
                            <p class="">Click me!</p>
                        </div>
                    </div>
                </div>
            {:else}
                <div class="absolute left-0 right-0 flex flex-col py-96 mb-[-37%] space-y-6 bottom-0 items-center justify-center align-middle">
                    <div class="rounded-2xl border-4 p-4 backdrop-blur-xl backdrop-brightness-[1.3] {!loaded ? 'pause' : ''}">
                        <h3 class="text-3xl">Press the key <span
                                class="text-4xl bg-white p-2 rounded-md">{current_key}</span> on your keyboard, then
                            click on the button below.</h3>
                    </div>
                    <div class="mt-3 animate-button {!loaded ? 'pause' : ''}">
                        <button class="border-2 p-4 text-xl rounded-md bg-white" onclick={() => {
                            if (required_keys.indexOf(current_key) === required_keys.length - 1) {
                                tutorial_ended = true;
                            } else {
                                current_key = required_keys[required_keys.indexOf(current_key) + 1];
                            }
                        }}>
                            Next
                        </button>
                        <div class="text-white
                        drop-shadow-2xl flex flex-col items-center space-y-1 animate-arrow {!loaded ? 'pause' : ''}">
                            <img src="/svg/up-arrow-svgrepo-com.svg" alt="up arrow" width="32" class="invert">
                            <p class="">Click me
                            </p>
                        </div>
                    </div>
                </div>
            {/if}
        </div>

        <div bind:this={handContainer} class="animate-hand">
            <div class="hand">
                <div class="absolute !scale-150 flex flex-row gap-64">
                    <div class="drop-shadow-2xl">
                        <Hand color="#394955" distance_between="400px" left={true}/>
                    </div>
                    <div class="drop-shadow-2xl">
                        <Hand color="#394955" distance_between="400px" left={false}/>
                    </div>
                </div>
            </div>
        </div>
    </div>
{:else}
    <div transition:fade>
        <video class="border-2 rounded-3xl w-full h-full overflow-clip bg-black" width="640" height="480"
               autoplay={true}
               bind:this={videoRef}></video>
    </div>
    <!--    </div>-->
{/if}

<style>
    @keyframes moveHand {
        0% {
            transform: translate(0, 0rem);
        }

        80% {
            transform: translate(0, -7rem);
        }

        90% {
            transform: translate(0, -7rem);
        }

        98% {
            transform: translate(0, 0rem);
        }
    }

    @keyframes appearText {
        0% {
            opacity: 0;
        }

        25% {
            opacity: 1;
        }

        95% {
            opacity: 1;
        }

        100% {
            opacity: 0;
        }
    }

    @keyframes appearButton {
        0% {
            opacity: 0;
        }

        40% {
            opacity: 0;
        }

        60% {
            opacity: 1;
        }

        95% {
            opacity: 1;
        }

        100% {
            opacity: 0;
        }
    }

    @keyframes appearArrow {
        0% {
            opacity: 1;
        }

        30% {
            opacity: 1;
        }

        50% {
            opacity: 0;
        }

        70% {
            opacity: 1;
        }

        100% {
            opacity: 1;
        }
    }

    .hand {
        transform: translate(23%, -3rem);
    }

    .animate-hand {
        animation: moveHand 14s infinite;
    }

    .animate-title {
        animation: appearText 14s infinite;
    }

    .animate-button {
        animation: appearButton 14s infinite;
    }

    .animate-arrow {
        animation: appearArrow 4s infinite;
    }

    .pause {
        animation-play-state: paused;
    }
</style>