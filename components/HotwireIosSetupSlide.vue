<template>
  <div class="hotwire-ios-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">🍏 iOS Integration</span>
      <span class="text-xs font-mono text-slate-400">Swift SDK</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between">
      <span>Adding Hotwire Native to iOS <span class="text-blue-400">(Swift) 🍏</span></span>
      
      <!-- Stepper Controls -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          v-for="step in [1, 2, 3]" 
          :key="step"
          @click="activeStep = step"
          :class="[
            'px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold',
            activeStep === step 
              ? 'bg-blue-950/80 border-blue-500 text-blue-300 shadow-lg scale-105 ring-1 ring-blue-500/50' 
              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
          ]">
          Step {{ step }}
        </button>
      </div>
    </h2>

    <!-- 2 Column Grid Layout: Left Stepper Explanations, Right Interactive Focused Code -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      
      <!-- Left Column: 3 Interactive Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-2.5">
        
        <!-- Step 1 Card -->
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-blue-500/60 shadow-lg ring-1 ring-blue-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 1 ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40' : 'bg-slate-800 text-slate-400']">1</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">1. Define Base Server URL</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Set your Rails app base URL endpoint.
              </p>
            </div>
          </div>
        </div>

        <!-- Step 2 Card -->
        <div 
          @click="activeStep = 2"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2 
              ? 'bg-slate-900 border-purple-500/60 shadow-lg ring-1 ring-purple-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 2 ? 'bg-purple-500/20 text-purple-300 border border-purple-500/40' : 'bg-slate-800 text-slate-400']">2</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">2. Initialize Hotwire Navigator</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Create <code class="text-purple-300 font-mono">Navigator(configuration:)</code> with start location.
              </p>
            </div>
          </div>
        </div>

        <!-- Step 3 Card -->
        <div 
          @click="activeStep = 3"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3 
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg ring-1 ring-emerald-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 3 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-slate-800 text-slate-400']">3</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">3. Connect Window & Route</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Set <code class="text-emerald-300 font-mono">rootViewController</code> and trigger <code class="text-emerald-300 font-mono">route(baseURL)</code>.
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- Right Column: Code Window with Focused Highlighting (Cols 6-12) -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
          <span class="text-blue-400 font-bold">ios/App/Delegates/SceneDelegate.swift</span>
          <span class="bg-slate-900 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold">Step {{ activeStep }} of 3</span>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed space-y-1 relative">
          <!-- Import lines (Dimmed) -->
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">import</span> <span class="text-amber-300">HotwireNative</span><br/>
            <span class="text-purple-400">import</span> <span class="text-blue-300">UIKit</span>
          </div>

          <!-- Line for Step 1: Base URL Definition -->
          <div :class="[
            'p-1.5 rounded transition-all duration-300',
            activeStep === 1 
              ? 'bg-blue-500/20 border-l-4 border-blue-400 text-white font-bold shadow-lg ring-1 ring-blue-500/30' 
              : 'opacity-30'
          ]">
            <span class="text-purple-400">let</span> baseURL = <span class="text-amber-300">URL</span>(string: <span class="text-emerald-300">"https://litloop.club/"</span>)!
          </div>

          <!-- Class Declaration (Dimmed) -->
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">class</span> <span class="text-amber-300">SceneDelegate</span>: <span class="text-blue-300">UIResponder</span>, <span class="text-blue-300">UIWindowSceneDelegate</span> {<br/>
            &nbsp;&nbsp;<span class="text-purple-400">var</span> window: <span class="text-blue-300">UIWindow</span>?
          </div>

          <!-- Line for Step 2: Navigator Initialization -->
          <div :class="[
            'p-1.5 rounded transition-all duration-300 pl-4',
            activeStep === 2 
              ? 'bg-purple-500/20 border-l-4 border-purple-400 text-white font-bold shadow-lg ring-1 ring-purple-500/30' 
              : 'opacity-30'
          ]">
            <span class="text-purple-400">private let</span> navigator = <span class="text-amber-300">Navigator</span>(configuration: .init(<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;name: <span class="text-emerald-300">"main"</span>, startLocation: baseURL.appending(path: <span class="text-emerald-300">"/"</span>)<br/>
            &nbsp;&nbsp;))
          </div>

          <!-- Method declaration header (Dimmed) -->
          <div :class="['transition-opacity duration-300 pl-4', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">func</span> <span class="text-blue-300">scene</span>(_ scene: <span class="text-blue-300">UIScene</span>, willConnectTo...) {
          </div>

          <!-- Line for Step 3: Root View & Route -->
          <div :class="[
            'p-1.5 rounded transition-all duration-300 pl-8',
            activeStep === 3 
              ? 'bg-emerald-500/20 border-l-4 border-emerald-400 text-white font-bold shadow-lg ring-1 ring-emerald-500/30' 
              : 'opacity-30'
          ]">
            window?.rootViewController = navigator.rootViewController<br/>
            navigator.route(baseURL)
          </div>

          <div :class="['transition-opacity duration-300 pl-4', activeStep ? 'opacity-40' : '']">}</div>
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">}</div>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeStep = ref(1)
</script>
