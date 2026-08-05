<template>
  <div class="monorepo-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">📁 LitLoop Monorepo</span>
      <span class="text-xs font-mono text-slate-400">https://litloop.club</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between">
      <span>Monorepo Setup: <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-blue-400">Rails + iOS + Android 📦</span></span>
      
      <!-- Interactive Project Selector Pills -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          @click="activeTab = 'backend'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'backend' ? 'bg-red-950/80 border-red-500 text-red-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          💎 Backend
        </button>

        <button 
          @click="activeTab = 'ios'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'ios' ? 'bg-blue-950/80 border-blue-500 text-blue-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          🍏 iOS
        </button>

        <button 
          @click="activeTab = 'android'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'android' ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          🤖 Android
        </button>
      </div>
    </h2>

    <!-- 2 Column Grid Layout: Left Interactive Monorepo Tree, Right Project Detail View -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
      
      <!-- Left Column: Interactive Monorepo Directory Tree (Cols 1-5) -->
      <div class="md:col-span-5 text-left">
        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-xs text-slate-300 space-y-2">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 text-[11px] text-slate-400">
            <span class="flex items-center gap-1.5 text-white font-bold">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              arif-nibaboch/
            </span>
            <span class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-amber-300">LitLoop Repo</span>
          </div>

          <!-- Directory Tree (Clickable Folders) -->
          <div class="space-y-2 text-[11px]">
            
            <!-- 1. Backend Folder -->
            <div 
              @click="activeTab = 'backend'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer space-y-1',
                activeTab === 'backend' 
                  ? 'bg-red-950/50 border-red-500 ring-1 ring-red-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-red-400 font-bold flex items-center justify-between">
                <span>💎 backend/</span>
                <span class="text-[9px] bg-red-900/60 px-1.5 py-0.5 rounded text-red-200">Rails Monolith</span>
              </div>
              <div class="pl-3 text-slate-400 text-[10px] space-y-0.5">
                <div>└── app/controllers/</div>
                <div class="text-amber-300 font-bold bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-800/60">
                  └── configurations_controller.rb ⚡
                </div>
              </div>
            </div>

            <!-- 2. iOS Folder -->
            <div 
              @click="activeTab = 'ios'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'ios' 
                  ? 'bg-blue-950/50 border-blue-500 ring-1 ring-blue-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-blue-400 font-bold flex items-center gap-1.5">
                <span>🍏 ios/</span>
              </div>
              <span class="text-[9px] text-blue-300 font-mono">LitLoop.xcodeproj</span>
            </div>

            <!-- 3. Android Folder -->
            <div 
              @click="activeTab = 'android'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'android' 
                  ? 'bg-emerald-950/50 border-emerald-500 ring-1 ring-emerald-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span>🤖 android/</span>
              </div>
              <span class="text-[9px] text-emerald-300 font-mono">et.netale.litloop</span>
            </div>

          </div>
        </div>
      </div>

      <!-- Right Column: Dynamic Project Code & Details View (Cols 6-12) -->
      <div class="md:col-span-7 text-left space-y-1.5">
        
        <!-- BACKEND DETAILS TAB -->
        <div v-if="activeTab === 'backend'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-amber-400 font-bold">backend/app/controllers/configurations_controller.rb</span>
            <span class="bg-red-950 text-red-300 px-2 py-0.5 rounded text-[10px] border border-red-800 font-bold">Rails Backend</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 shadow-2xl font-mono text-[10.5px] text-amber-300 overflow-x-auto leading-relaxed h-[240px]">
            <div class="text-purple-400">class <span class="text-amber-300">ConfigurationsController</span> &lt; <span class="text-blue-300">ApplicationController</span></div>
            <div class="pl-4 text-purple-400">def <span class="text-blue-300">ios_v1</span></div>
            <div class="pl-8 text-slate-300">render <span class="text-emerald-400">json:</span> { rules: [{ patterns: [<span class="text-emerald-300">"/new$"</span>, <span class="text-emerald-300">"/edit$"</span>], properties: { context: <span class="text-emerald-300">"modal"</span> } }] }</div>
            <div class="pl-4 text-purple-400">end</div>
            <br/>
            <div class="pl-4 text-purple-400">def <span class="text-blue-300">android_v1</span></div>
            <div class="pl-8 text-slate-300">render <span class="text-emerald-400">json:</span> {</div>
            <div class="pl-12 text-slate-300">rules: [</div>
            <div class="pl-16 text-slate-400">{ patterns: [<span class="text-emerald-300">".*"</span>], properties: { uri: <span class="text-emerald-300">"hotwire://fragment/web"</span>, pull_to_refresh_enabled: <span class="text-purple-400">true</span> } },</div>
            <div class="pl-16 text-slate-400">{ patterns: [<span class="text-emerald-300">"/new$"</span>, <span class="text-emerald-300">"/edit$"</span>], properties: { context: <span class="text-emerald-300">"modal"</span> } }</div>
            <div class="pl-12 text-slate-300">]</div>
            <div class="pl-8 text-slate-300">}</div>
            <div class="pl-4 text-purple-400">end</div>
            <div class="text-purple-400">end</div>
          </div>
        </div>

        <!-- IOS DETAILS TAB -->
        <div v-if="activeTab === 'ios'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-blue-400 font-bold">ios/App/Delegates/SceneDelegate.swift</span>
            <span class="bg-blue-950 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-blue-800 font-bold">iOS Swift</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 shadow-2xl font-mono text-[10.5px] text-slate-300 overflow-x-auto leading-relaxed h-[240px]">
            <div><span class="text-purple-400">import</span> <span class="text-amber-300">HotwireNative</span></div>
            <div><span class="text-purple-400">import</span> <span class="text-blue-300">UIKit</span></div>
            <br/>
            <div><span class="text-purple-400">let</span> baseURL = <span class="text-amber-300">URL</span>(string: <span class="text-emerald-300">"https://litloop.club/"</span>)!</div>
            <br/>
            <div><span class="text-purple-400">class</span> <span class="text-amber-300">SceneDelegate</span>: <span class="text-blue-300">UIResponder</span>, <span class="text-blue-300">UIWindowSceneDelegate</span> {</div>
            <div class="pl-4 text-slate-400"><span class="text-purple-400">var</span> window: <span class="text-blue-300">UIWindow</span>?</div>
            <div class="pl-4 text-purple-400">private let <span class="text-slate-200">navigator</span> = <span class="text-amber-300">Navigator</span>(configuration: .init(</div>
            <div class="pl-8 text-slate-300">name: <span class="text-emerald-300">"main"</span>,</div>
            <div class="pl-8 text-emerald-400">startLocation: baseURL.appending(path: <span class="text-emerald-300">"/"</span>)</div>
            <div class="pl-4 text-purple-400">))</div>
            <br/>
            <div class="pl-4 text-purple-400">func <span class="text-blue-300">scene</span>(_ scene: <span class="text-blue-300">UIScene</span>, willConnectTo...) {</div>
            <div class="pl-8 text-slate-300">window?.rootViewController = navigator.rootViewController</div>
            <div class="pl-8 text-emerald-400">navigator.route(baseURL)</div>
            <div class="pl-4 text-purple-400">}</div>
            <div>}</div>
          </div>
        </div>

        <!-- ANDROID DETAILS TAB -->
        <div v-if="activeTab === 'android'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-emerald-400 font-bold">android/app/.../et/netale/litloop/MainActivity.kt</span>
            <span class="bg-emerald-950 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-emerald-800 font-bold">Android Kotlin</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 shadow-2xl font-mono text-[10.5px] text-slate-300 overflow-x-auto leading-relaxed h-[240px]">
            <div><span class="text-purple-400">package</span> <span class="text-emerald-300">et.netale.litloop</span></div>
            <br/>
            <div><span class="text-purple-400">import</span> <span class="text-amber-300">dev.hotwire.navigation.activities.HotwireActivity</span></div>
            <div><span class="text-purple-400">import</span> <span class="text-amber-300">dev.hotwire.navigation.navigator.NavigatorConfiguration</span></div>
            <br/>
            <div><span class="text-purple-400">const val</span> baseURL = <span class="text-emerald-300">"https://litloop.club"</span></div>
            <br/>
            <div><span class="text-purple-400">class</span> <span class="text-amber-300">MainActivity</span> : <span class="text-emerald-300">HotwireActivity</span>() {</div>
            <div class="pl-4 text-purple-400">override fun <span class="text-blue-300">navigatorConfigurations</span>(): List&lt;NavigatorConfiguration&gt; {</div>
            <div class="pl-8 text-purple-400">return <span class="text-slate-200">listOf</span>(</div>
            <div class="pl-12 text-amber-300">NavigatorConfiguration(</div>
            <div class="pl-16 text-slate-300">name = <span class="text-emerald-300">"main"</span>,</div>
            <div class="pl-16 text-emerald-400">startLocation = <span class="text-emerald-300">"$baseURL/users/sign_in"</span>,</div>
            <div class="pl-16 text-slate-300">navigatorHostId = <span class="text-blue-300">R.id.main</span></div>
            <div class="pl-12 text-amber-300">)</div>
            <div class="pl-8 text-slate-300">)</div>
            <div class="pl-4 text-purple-400">}</div>
            <div>}</div>
          </div>
        </div>

      </div>

    </div>

    <!-- Bottom Dynamic Takeaway Banner -->
    <div class="mt-3 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs">
      <span class="text-slate-300">
        <template v-if="activeTab === 'backend'">
          💡 <strong>Rails Path Config:</strong> Serves navigation rules (<code class="text-amber-300">/configurations/ios_v1</code>) directly to both clients.
        </template>
        <template v-if="activeTab === 'ios'">
          🍏 <strong>iOS Client:</strong> Swift <code class="text-blue-300">SceneDelegate</code> binds Hotwire <code class="text-blue-300">Navigator</code> to <code class="text-blue-300">https://litloop.club</code>.
        </template>
        <template v-if="activeTab === 'android'">
          🤖 <strong>Android Client:</strong> Kotlin <code class="text-emerald-300">MainActivity</code> extends <code class="text-emerald-300">HotwireActivity</code> to manage fragment backstack.
        </template>
      </span>

      <span :class="['text-[10px] font-mono px-2 py-0.5 rounded border shrink-0 font-bold ml-2', activeTab === 'backend' ? 'bg-red-950 text-red-300 border-red-700' : activeTab === 'ios' ? 'bg-blue-950 text-blue-300 border-blue-700' : 'bg-emerald-950 text-emerald-300 border-emerald-700']">
        LitLoop {{ activeTab.toUpperCase() }} ⚡
      </span>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('backend')
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
