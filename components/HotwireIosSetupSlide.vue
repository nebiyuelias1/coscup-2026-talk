<template>
  <div class="hotwire-ios-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">🍏 LitLoop iOS Integration</span>
      <span class="text-xs font-mono text-slate-400">https://litloop.club</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-3 text-left flex items-center justify-between">
      <span>Adding Hotwire Native to iOS <span class="text-blue-400">(Swift) 🍏</span></span>
      <span class="text-xs font-mono text-blue-300 bg-blue-950/80 px-2.5 py-1 rounded border border-blue-800">
        LitLoop iOS Setup 📦
      </span>
    </h2>

    <!-- 2 Column Grid Layout: Left Setup Steps, Right Swift Code Snippet -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      
      <!-- Left Column: Setup Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-3">
        <div class="bg-slate-900/90 border border-blue-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-blue-400 m-0 flex items-center gap-1.5">
            <span>1. Set Base URL</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Define your LitLoop server URL:<br/>
            <code class="text-blue-300 font-mono text-[10px]">https://litloop.club/</code>
          </p>
        </div>

        <div class="bg-slate-900/90 border border-purple-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-purple-300 m-0 flex items-center gap-1.5">
            <span>2. Configure Hotwire Navigator</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Initialize <code class="text-purple-300 font-mono text-[10px]">Navigator(configuration:)</code> with start location.
          </p>
        </div>

        <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-emerald-400 m-0 flex items-center gap-1.5">
            <span>3. Connect SceneDelegate Window</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Attach root controller and route to <code class="text-emerald-300 font-mono text-[10px]">baseURL</code> inside <code class="text-slate-200 font-mono text-[10px]">willConnectTo</code>.
          </p>
        </div>
      </div>

      <!-- Right Column: Real SceneDelegate.swift Code Snippet (Cols 6-12) -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
          <span class="text-blue-400 font-bold">ios/App/Delegates/SceneDelegate.swift</span>
          <span class="bg-slate-900 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold">LitLoop Swift</span>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed">
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

    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="mt-3 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs">
      <span class="text-slate-300">
        ⚡ <strong>LitLoop iOS Setup:</strong> Swift SceneDelegate initializes Hotwire Native and routes directly to <code class="text-blue-300">https://litloop.club</code>.
      </span>
      <span class="text-[10px] font-mono text-blue-400 bg-blue-950/80 px-2 py-0.5 rounded border border-blue-700 shrink-0 font-bold ml-2">
        LitLoop iOS 🍏
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
