<template>
  <div class="dynamic-native-title-slide w-full my-auto flex flex-col justify-center">
    <!-- Header with Stepper Controls -->
    <h2 class="text-2xl font-black tracking-tight text-white mb-3 text-left flex items-center justify-between">
      <span>Dynamic Native Titles: <span class="text-red-500">content_for(:title) 🏷️</span></span>
      
      <!-- Stepper Buttons -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          v-for="step in [1, 2, 3]" 
          :key="step"
          @click="activeStep = step"
          :class="[
            'px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold',
            activeStep === step 
              ? 'bg-amber-950/80 border-amber-500 text-amber-300 shadow-lg scale-105 ring-1 ring-amber-500/50' 
              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
          ]">
          Step {{ step }}
        </button>
      </div>
    </h2>

    <!-- 2 Column Grid Layout: Left Stepper Cards, Right Focused Code Window -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      
      <!-- Left Column: 3 Interactive Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-2.5">
        
        <!-- Step 1 Card -->
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-red-500/60 shadow-lg ring-1 ring-red-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-60 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 1 ? 'bg-red-500/20 text-red-400 border border-red-500/40' : 'bg-slate-800 text-slate-400']">1</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">1. Set Title in View</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Pass page title in ERB: <code class="text-red-300 font-mono">content_for :title</code>.
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
              ? 'bg-slate-900 border-amber-500/60 shadow-lg ring-1 ring-amber-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-60 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 2 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40' : 'bg-slate-800 text-slate-400']">2</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">2. Render HTML &lt;title&gt;</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Layout prints title dynamically in HTML head.
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
              ? 'bg-slate-900 border-blue-500/60 shadow-lg ring-1 ring-blue-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-60 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 3 ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40' : 'bg-slate-800 text-slate-400']">3</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">3. Auto Sync Native Header</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                Hotwire Native updates Swift & Kotlin top bars.
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- Right Column: Code & Flow Window with Noise Suppression (Cols 6-12) -->
      <div class="md:col-span-7 space-y-2">
        
        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 space-y-2 relative">
          
          <!-- STEP 1: View Template ERB (Focused when activeStep === 1) -->
          <div :class="[
            'p-2.5 rounded transition-all duration-300 border',
            activeStep === 1 
              ? 'bg-red-950/50 border-red-500/80 shadow-lg ring-1 ring-red-500/40 opacity-100 scale-[1.01]' 
              : 'bg-slate-900/40 border-slate-800/60 opacity-30 blur-[0.2px]'
          ]">
            <div class="text-[10px] text-slate-400 pb-1">app/views/books/show.html.erb</div>
            <div class="text-red-400 font-bold">
              &lt;%= <span class="text-amber-300">content_for</span> <span class="text-emerald-300">:title</span>, <span class="text-emerald-300">@book.title</span> %&gt;
            </div>
          </div>

          <!-- STEP 2: Application Layout HTML (Focused when activeStep === 2) -->
          <div :class="[
            'p-2.5 rounded transition-all duration-300 border',
            activeStep === 2 
              ? 'bg-amber-950/50 border-amber-500/80 shadow-lg ring-1 ring-amber-500/40 opacity-100 scale-[1.01]' 
              : 'bg-slate-900/40 border-slate-800/60 opacity-30 blur-[0.2px]'
          ]">
            <div class="text-[10px] text-slate-400 pb-1">app/views/layouts/application.html.erb</div>
            <div class="text-purple-400 font-bold">
              &lt;<span class="text-amber-300">title</span>&gt;
              <span class="text-red-400">&lt;%=</span> <span class="text-slate-200">content_for?(:title) ? content_for(:title) : "LitLoop"</span> <span class="text-red-400">%&gt;</span>
              &lt;/<span class="text-amber-300">title</span>&gt;
            </div>
          </div>

          <!-- STEP 3: Native Handlers (Focused when activeStep === 3) -->
          <div :class="[
            'p-2.5 rounded transition-all duration-300 border space-y-1.5',
            activeStep === 3 
              ? 'bg-blue-950/50 border-blue-500/80 shadow-lg ring-1 ring-blue-500/40 opacity-100 scale-[1.01]' 
              : 'bg-slate-900/40 border-slate-800/60 opacity-30 blur-[0.2px]'
          ]">
            <div class="text-[10px] text-blue-300 font-bold flex items-center justify-between">
              <span>Hotwire Native Bridge (iOS & Android)</span>
              <span class="text-[9px] text-emerald-400">Auto Sync</span>
            </div>
            <div class="text-[10.5px] text-slate-300 font-mono">
              🍏 <span class="text-purple-400">navigationItem</span>.title = <span class="text-emerald-300">webView.title</span><br/>
              🤖 <span class="text-purple-400">toolbar</span>.title = <span class="text-emerald-300">webView.title</span>
            </div>
          </div>

        </div>

      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeStep = ref(1)
</script>
