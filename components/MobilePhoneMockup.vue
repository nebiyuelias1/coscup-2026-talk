<template>
  <div class="mobile-phone-mockup flex flex-col items-center justify-center my-2">
    <!-- Interactive Control Pills -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-3 z-10">
      <button 
        @click="activeTab = 'web'" 
        :class="['px-3 py-1 rounded-full text-xs font-bold transition-all', activeTab === 'web' ? 'bg-red-600 text-white shadow-lg shadow-red-900/50 scale-105' : 'bg-slate-800 text-slate-400 hover:text-white']">
        🌐 1. Server HTML (Rails View)
      </button>
      <button 
        @click="activeTab = 'native'" 
        :class="['px-3 py-1 rounded-full text-xs font-bold transition-all', activeTab === 'native' ? 'bg-blue-600 text-white shadow-lg shadow-blue-900/50 scale-105' : 'bg-slate-800 text-slate-400 hover:text-white']">
        📱 2. Native Nav Stack
      </button>
      <button 
        @click="activeTab = 'strada'" 
        :class="['px-3 py-1 rounded-full text-xs font-bold transition-all', activeTab === 'strada' ? 'bg-purple-600 text-white shadow-lg shadow-purple-900/50 scale-105' : 'bg-slate-800 text-slate-400 hover:text-white']">
        🌉 3. Strada Bridge
      </button>
    </div>

    <!-- Phone Hardware Mockup -->
    <div class="relative w-[300px] h-[520px] bg-slate-950 rounded-[40px] p-3 border-4 border-slate-700 shadow-2xl shadow-red-950/30 overflow-hidden flex flex-col">
      <!-- Phone Notch / Dynamic Island -->
      <div class="absolute top-2 left-1/2 -translate-x-1/2 w-28 h-5 bg-slate-900 rounded-full z-30 flex items-center justify-center gap-2">
        <div class="w-2.5 h-2.5 rounded-full bg-slate-950"></div>
        <div class="w-1.5 h-1.5 rounded-full bg-blue-900/60"></div>
      </div>

      <!-- Native Status Bar -->
      <div class="w-full pt-2 pb-1 px-4 flex items-center justify-between text-[10px] text-slate-400 font-mono font-bold z-20">
        <span>9:41</span>
        <div class="flex items-center gap-1">
          <span>5G</span>
          <span>100%</span>
        </div>
      </div>

      <!-- Native App Navigation Header -->
      <div class="bg-slate-900/90 border-b border-slate-800 px-3 py-2 flex items-center justify-between text-xs font-bold text-white z-20">
        <span class="text-red-400 flex items-center gap-1 font-mono">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          Hotwire Native
        </span>
        <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded">Rails 8</span>
      </div>

      <!-- Screen Content Viewport -->
      <div class="flex-1 bg-slate-900 overflow-y-auto p-3 text-left relative flex flex-col justify-between">
        
        <!-- MODE 1: Web / HTML over the wire -->
        <div v-if="activeTab === 'web'" class="space-y-2 animate-fade-in">
          <div class="p-2 bg-red-950/40 border border-red-800/40 rounded-lg">
            <span class="text-[10px] font-mono uppercase tracking-wider text-red-400 block font-bold">Rails Server Rendered HTML</span>
            <h4 class="text-sm font-bold text-white m-0">Feed Items</h4>
          </div>

          <div v-for="i in 3" :key="i" class="p-2.5 bg-slate-800/80 rounded-lg border border-slate-700/50 flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-full bg-gradient-to-br from-red-500 to-amber-500 flex items-center justify-center font-bold text-white text-xs">
              #{{ i }}
            </div>
            <div class="flex-1 min-w-0">
              <div class="text-xs font-semibold text-white truncate">Hotwire Native Feed Item</div>
              <div class="text-[10px] text-slate-400">Rendered via Turbo Frames</div>
            </div>
            <span class="text-[10px] text-red-400 font-mono font-bold">200 OK</span>
          </div>

          <div class="p-2 bg-blue-950/40 border border-blue-800/40 rounded-lg text-[11px] text-blue-300">
            💡 Zero App Store updates needed when changing web views!
          </div>
        </div>

        <!-- MODE 2: Native Navigation -->
        <div v-if="activeTab === 'native'" class="space-y-2 animate-fade-in">
          <div class="p-2 bg-blue-950/40 border border-blue-800/40 rounded-lg">
            <span class="text-[10px] font-mono uppercase tracking-wider text-blue-400 block font-bold">Native iOS/Android Navigation</span>
            <h4 class="text-sm font-bold text-white m-0">Path Configuration</h4>
          </div>

          <div class="p-3 bg-slate-800/90 rounded-lg border border-blue-500/40 space-y-2">
            <div class="flex items-center justify-between text-xs font-bold text-slate-200">
              <span>/posts/new</span>
              <span class="px-2 py-0.5 rounded bg-blue-600 text-white text-[10px]">Present Modal</span>
            </div>
            <p class="text-[11px] text-slate-300">
              Hotwire intercepts link clicks and opens a <strong>Native iOS Sheet</strong> with native swipe-to-dismiss!
            </p>
          </div>

          <div class="p-2 bg-slate-950/80 rounded font-mono text-[10px] text-blue-300 border border-slate-800">
            json: { "patterns": ["/new$"], "properties": { "presentation": "modal" } }
          </div>
        </div>

        <!-- MODE 3: Strada Bridge -->
        <div v-if="activeTab === 'strada'" class="space-y-2 animate-fade-in">
          <div class="p-2 bg-purple-950/40 border border-purple-800/40 rounded-lg">
            <span class="text-[10px] font-mono uppercase tracking-wider text-purple-400 block font-bold">Strada Component Bridge</span>
            <h4 class="text-sm font-bold text-white m-0">HTML -> Native Call</h4>
          </div>

          <div class="p-3 bg-slate-800/90 rounded-lg border border-purple-500/40 space-y-2 text-center">
            <p class="text-[11px] text-purple-200 font-medium">
              HTML element with <code>data-bridge-components="form"</code>
            </p>
            <button 
              @click="showNativeToast = true" 
              class="w-full py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded font-bold text-xs shadow hover:brightness-110 active:scale-95 transition-all">
              ⚡ Trigger Native Haptic and Sheet
            </button>
          </div>

          <!-- Native Toast Notification overlay mockup -->
          <div v-if="showNativeToast" class="p-2 bg-emerald-950 border border-emerald-500/50 rounded-lg text-center animate-bounce">
            <span class="text-xs font-bold text-emerald-300">✅ Native Swift / Kotlin Code Executed!</span>
          </div>
        </div>

        <!-- Phone Bottom Tab Bar -->
        <div class="pt-2 mt-2 border-t border-slate-800 flex justify-around items-center text-[10px] text-slate-400">
          <div class="flex flex-col items-center text-red-400 font-bold">
            <span>🏠</span>
            <span>Feed</span>
          </div>
          <div class="flex flex-col items-center hover:text-white">
            <span>🔍</span>
            <span>Search</span>
          </div>
          <div class="flex flex-col items-center hover:text-white">
            <span>⚡</span>
            <span>Strada</span>
          </div>
          <div class="flex flex-col items-center hover:text-white">
            <span>👤</span>
            <span>Profile</span>
          </div>
        </div>

      </div>

      <!-- Home Bar Indicator -->
      <div class="w-32 h-1 bg-slate-600 rounded-full mx-auto my-1"></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('web')
const showNativeToast = ref(false)
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.25s ease-out forwards;
}
</style>
