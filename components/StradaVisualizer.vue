<template>
  <div class="strada-visualizer bg-slate-950 border border-purple-500/30 rounded-xl p-4 my-2 text-left font-mono text-xs">
    <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-3">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-purple-500 animate-pulse"></span>
        <span class="text-purple-300 font-bold">Strada Bridge Flow</span>
      </div>
      <span class="text-[10px] bg-purple-950 text-purple-200 px-2 py-0.5 rounded border border-purple-800">
        HTML ⇄ Native Swift/Kotlin
      </span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
      <!-- Step 1: Rails View -->
      <div class="p-3 bg-slate-900 rounded-lg border border-slate-800">
        <div class="text-[10px] text-red-400 font-bold uppercase mb-1">1. Rails ERB View</div>
        <div class="bg-slate-950 p-2 rounded text-[11px] text-amber-300 overflow-x-auto">
          &lt;button<br>
          &nbsp;&nbsp;data-bridge-component="form"<br>
          &nbsp;&nbsp;data-bridge-title="Save"&gt;<br>
          &nbsp;&nbsp;Submit<br>
          &lt;/button&gt;
        </div>
      </div>

      <!-- Step 2: Strada Bridge JS -->
      <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 flex flex-col justify-between">
        <div>
          <div class="text-[10px] text-purple-400 font-bold uppercase mb-1">2. Strada Bridge Event</div>
          <div class="bg-slate-950 p-2 rounded text-[10px] text-purple-300">
            postMessage({<br/>
            &nbsp;&nbsp;"component": "form",<br/>
            &nbsp;&nbsp;"event": "connect",<br/>
            &nbsp;&nbsp;"data": { "title": "Save" }<br/>
            })
          </div>
        </div>
        <div class="text-[10px] text-center text-purple-400 mt-2 font-sans font-semibold">⚡ Automatic Message Passing</div>
      </div>

      <!-- Step 3: Native Swift/Kotlin -->
      <div class="p-3 bg-slate-900 rounded-lg border border-slate-800">
        <div class="text-[10px] text-blue-400 font-bold uppercase mb-1">3. Native Component</div>
        <div class="bg-slate-950 p-2 rounded text-[10px] text-blue-300">
          class FormComponent:<br/>
          &nbsp;&nbsp;BridgeComponent {<br/>
          &nbsp;&nbsp;func onConnect() {<br/>
          &nbsp;&nbsp;&nbsp;&nbsp;showNativeButton()<br/>
          &nbsp;&nbsp;}<br/>
          }
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
