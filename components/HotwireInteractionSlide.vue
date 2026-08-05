<template>
  <div class="hotwire-interaction-slide w-full my-auto flex flex-col justify-center">
    
    <!-- Title Header -->
    <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
      How the Interaction Works 🔄
    </h2>

    <!-- Main Content Layout Grid -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-stretch">
      
      <!-- Left Column: 3 Step Cards (Cols 1-5) -->
      <div class="md:col-span-5 space-y-2.5 text-left flex flex-col justify-between">
        
        <!-- Step 1 Card -->
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-amber-500/60 shadow-lg shadow-amber-950/40 ring-1 ring-amber-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0 transition-colors', activeStep === 1 ? 'bg-amber-500/20 text-amber-400 border border-amber-500/40' : 'bg-slate-800 text-slate-400']">
              1
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">User Taps a Link</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                In <strong>LitLoop</strong>, tapping a book card interrupts default web reload and hands navigation to Hotwire Native.
              </p>
            </div>
          </div>
          <div v-if="activeStep === 1" class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-amber-500 to-amber-300"></div>
        </div>

        <!-- Step 2 Card -->
        <div 
          @click="activeStep = 2"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2 
              ? 'bg-slate-900 border-blue-500/60 shadow-lg shadow-blue-950/40 ring-1 ring-blue-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0 transition-colors', activeStep === 2 ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40' : 'bg-slate-800 text-slate-400']">
              2
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">Native Nav First</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                The iOS or Android app <strong>pushes a new native screen</strong> with smooth native transitions instantly.
              </p>
            </div>
          </div>
          <div v-if="activeStep === 2" class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-blue-500 to-blue-300"></div>
        </div>

        <!-- Step 3 Card -->
        <div 
          @click="activeStep = 3"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3 
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg shadow-emerald-950/40 ring-1 ring-emerald-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0 transition-colors', activeStep === 3 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-slate-800 text-slate-400']">
              3
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">HTML Renders Inside</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                The native controller fetches HTML from <code class="text-emerald-300 font-mono text-[10px]">litloop.club/books/42</code> and renders it inside the native view.
              </p>
            </div>
          </div>
          <div v-if="activeStep === 3" class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-emerald-500 to-emerald-300"></div>
        </div>

      </div>

      <!-- Right Column: Interactive Phone & Visual Flow Diagram (Cols 6-12) -->
      <div class="md:col-span-7 bg-slate-950/90 border border-slate-800 rounded-xl p-4 flex flex-col justify-between relative overflow-hidden shadow-2xl">
        
        <!-- Background Ambient Glow -->
        <div 
          :class="[
            'absolute -top-20 -right-20 w-64 h-64 rounded-full blur-3xl pointer-events-none transition-all duration-500',
            activeStep === 1 ? 'bg-amber-600/15' : activeStep === 2 ? 'bg-blue-600/15' : 'bg-emerald-600/15'
          ]">
        </div>

        <!-- Interactive Graphical Demonstration Screen -->
        <div class="flex-1 flex items-center justify-center py-4 px-1">
          
          <!-- STEP 1 GRAPHIC: User Taps Book Link in LitLoop -->
          <div v-if="activeStep === 1" class="w-full grid grid-cols-12 gap-3 items-center animate-fade-in">
            <!-- Simulated Mobile Screen -->
            <div class="col-span-6 bg-slate-900 border-2 border-amber-500/50 rounded-2xl p-2.5 text-left shadow-xl relative overflow-hidden">
              <div class="flex items-center justify-between border-b border-slate-800 pb-1.5 mb-2 text-[10px] text-slate-400">
                <span class="font-bold text-amber-400">LitLoop Feed</span>
                <span>/books</span>
              </div>
              
              <div class="space-y-2">
                <div class="p-2 bg-slate-800/90 rounded-lg border border-slate-700/60 text-[10px]">
                  <div class="text-slate-300 font-medium mb-1">📖 Currently Reading</div>
                  
                  <!-- Book Link Button with Tap Gesture Ripple -->
                  <div class="relative inline-block w-full">
                    <div class="p-2 rounded bg-amber-500/20 border border-amber-400/80 text-amber-200 font-bold flex items-center justify-between">
                      <span class="text-[10px] text-amber-100 truncate">👉 The Midnight Library</span>
                      <span class="text-[9px] bg-amber-500 text-slate-950 px-1.5 py-0.5 rounded font-mono font-black">TAP!</span>
                    </div>
                    <!-- Animated Tap Circle Ripple -->
                    <div class="absolute right-3 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full border-2 border-amber-400 animate-ping pointer-events-none"></div>
                  </div>
                </div>
                
                <div class="p-1.5 bg-slate-950 rounded text-[9px] font-mono text-slate-400 truncate">
                  &lt;a href="/books/42"&gt;The Midnight Library&lt;/a&gt;
                </div>
              </div>
            </div>

            <!-- Intercept Process Graphic -->
            <div class="col-span-6 space-y-2 text-left">
              <div class="p-2.5 bg-amber-950/40 border border-amber-500/40 rounded-xl">
                <div class="text-[10px] font-mono font-bold text-amber-400 uppercase mb-1">Link Click Intercepted</div>
                <div class="text-[11px] text-slate-200 leading-snug">
                  Intercepts link click to <code class="text-amber-300 font-mono text-[10px]">/books/42</code> and passes URL to native navigator.
                </div>
              </div>

              <div class="p-2 bg-slate-900 border border-slate-800 rounded-lg text-[10px] font-mono text-amber-300">
                <div>// Hotwire Native Delegate</div>
                <div class="text-slate-400">navigator.route("https://litloop.club/books/42")</div>
              </div>
            </div>
          </div>

          <!-- STEP 2 GRAPHIC: Native Navigation Push -->
          <div v-if="activeStep === 2" class="w-full grid grid-cols-12 gap-3 items-center animate-fade-in">
            <!-- Navigation Stack Visualization -->
            <div class="col-span-7 space-y-2 relative">
              <!-- Stack Container representation -->
              <div class="bg-slate-900/90 border border-blue-500/40 rounded-xl p-3 text-left relative overflow-hidden">
                <div class="text-[10px] font-mono font-bold text-blue-400 uppercase mb-2 flex items-center justify-between">
                  <span>Native Stack Push</span>
                </div>

                <div class="flex items-center gap-2 relative">
                  <!-- Previous Screen (Pushed back) -->
                  <div class="w-1/3 bg-slate-800/60 border border-slate-700 rounded-lg p-2 opacity-50 scale-95">
                    <div class="text-[9px] font-bold text-slate-400">/books</div>
                    <div class="text-[8px] text-slate-500 truncate">Book Feed</div>
                  </div>

                  <!-- Animated Push Arrow -->
                  <div class="text-blue-400 text-lg font-bold animate-bounce">➔</div>

                  <!-- New Native Screen (Pushed in) -->
                  <div class="w-3/5 bg-slate-900 border-2 border-blue-400 rounded-lg p-2.5 shadow-xl ring-2 ring-blue-500/30 transform translate-x-0 transition-all">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-1 mb-1">
                      <span class="text-[10px] font-bold text-blue-300">/books/42</span>
                      <span class="w-1.5 h-1.5 rounded-full bg-blue-400 animate-pulse"></span>
                    </div>
                    <div class="text-[10px] text-slate-300 font-semibold">LitLoop Native Controller</div>
                    <div class="text-[9px] text-blue-400 font-mono">UINavigationController / Fragment</div>
                  </div>
                </div>
              </div>

              <div class="p-2 bg-blue-950/40 border border-blue-800/40 rounded-lg text-left text-[10px] text-blue-200">
                Native navbar & slide animation display immediately before HTML network response returns.
              </div>
            </div>

            <!-- Native Stack Spec Card -->
            <div class="col-span-5 text-left space-y-2">
              <div class="p-2 bg-slate-900 border border-slate-800 rounded-lg text-[10px] font-mono text-blue-300">
                <span class="text-slate-500">// Swift / Kotlin</span><br/>
                <span class="text-purple-400">navigator</span>.route(<span class="text-emerald-300">"https://litloop.club/books/42"</span>)
              </div>
              <div class="p-2 bg-slate-900 border border-slate-800 rounded-lg text-[10px] text-slate-300">
                Native back button & swipe gestures work out of the box.
              </div>
            </div>
          </div>

          <!-- STEP 3 GRAPHIC: LitLoop HTML Renders Inside Frame -->
          <div v-if="activeStep === 3" class="w-full grid grid-cols-12 gap-3 items-center animate-fade-in">
            <!-- Rails Server -> Native Frame Flow -->
            <div class="col-span-6 bg-slate-900 border border-slate-800 rounded-xl p-2.5 text-left space-y-2">
              <div class="flex items-center justify-between text-[10px] font-mono font-bold text-red-400 border-b border-slate-800 pb-1">
                <span>LitLoop Rails Server</span>
                <span class="text-emerald-400">200 OK</span>
              </div>
              <div class="bg-slate-950 p-2 rounded border border-slate-800 text-[10px] font-mono text-amber-300 leading-tight">
                &lt;div class="book-details"&gt;<br/>
                &nbsp;&nbsp;&lt;h1&gt;The Midnight Library&lt;/h1&gt;<br/>
                &nbsp;&nbsp;&lt;p&gt;by Matt Haig&lt;/p&gt;<br/>
                &lt;/div&gt;
              </div>
              <div class="text-[10px] text-slate-400 flex items-center justify-between">
                <span>Response Time:</span>
                <span class="text-emerald-400 font-mono font-bold">~25ms</span>
              </div>
            </div>

            <!-- Flow Arrow -->
            <div class="col-span-1 text-emerald-400 font-bold text-xl flex items-center justify-center">
              ⚡
            </div>

            <!-- Final Rendered Native View -->
            <div class="col-span-5 bg-slate-900 border-2 border-emerald-500/60 rounded-xl p-2.5 text-left shadow-lg">
              <div class="flex items-center justify-between border-b border-slate-800 pb-1 mb-1.5">
                <span class="text-[10px] font-bold text-emerald-400">Rendered Screen</span>
                <span class="text-[9px] text-emerald-300 font-mono">HTML Loaded</span>
              </div>
              <div class="p-2 bg-slate-800 rounded text-left space-y-1">
                <h4 class="text-xs font-bold text-white m-0">The Midnight Library</h4>
                <p class="text-[10px] text-slate-300 m-0">4.5/5 ⭐ by Matt Haig</p>
              </div>
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

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
