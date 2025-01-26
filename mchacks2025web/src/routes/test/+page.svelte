<script>
    import {messages, connectWebSocket, sendMessage} from "$lib/websocket";
    import {onMount} from "svelte";

    let input = "";

    onMount(() => {
        connectWebSocket("ws://localhost:8000/ws");
    });
</script>

<main>
    <h1>WebSocket Client</h1>
    <input
            type="text"
            bind:value={input}
            placeholder="Enter a message"
            on:keypress={(e) => e.key === 'Enter' && sendMessage(input)}
    />
    <button on:click={() => sendMessage(input)}>Send</button>

    <h2>Messages:</h2>
    <ul>
        {#each $messages as msg}
            <li>{msg}</li>
        {/each}
    </ul>
</main>

<style>
    main {
        text-align: center;
        padding: 2rem;
        max-width: 600px;
        margin: 0 auto;
    }

    input {
        padding: 0.5rem;
        margin-right: 0.5rem;
    }
</style>
