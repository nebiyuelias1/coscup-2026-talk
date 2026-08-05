<template>
  <div class="hotwire-android-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">🤖 LitLoop Android Integration</span>
      <span class="text-xs font-mono text-slate-400">https://litloop.club</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-3 text-left flex items-center justify-between">
      <span>Adding Hotwire Native to Android <span class="text-emerald-400">(Kotlin) 🤖</span></span>
      <span class="text-xs font-mono text-emerald-300 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-800">
        LitLoop Android Setup 📦
      </span>
    </h2>

    <!-- 2 Column Grid Layout: Left Setup Steps, Right Kotlin Code Snippet -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      
      <!-- Left Column: Setup Steps (Cols 1-5) -->
      <div class="md:col-span-5 space-y-3">
        <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-emerald-400 m-0 flex items-center gap-1.5">
            <span>1. Set Base URL</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Define production URL for LitLoop:<br/>
            <code class="text-emerald-300 font-mono text-[10px]">const val baseURL = "https://litloop.club"</code>
          </p>
        </div>

        <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-amber-400 m-0 flex items-center gap-1.5">
            <span>2. Subclass HotwireActivity</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Extend <code class="text-amber-300 font-mono text-[10px]">HotwireActivity</code> in package <code class="text-slate-200 font-mono text-[10px]">et.netale.litloop</code>.
          </p>
        </div>

        <div class="bg-slate-900/90 border border-blue-500/30 rounded-xl p-3.5 shadow-lg space-y-1">
          <h4 class="text-xs font-bold text-blue-400 m-0 flex items-center gap-1.5">
            <span>3. Configure Navigator</span>
          </h4>
          <p class="text-[11px] text-slate-300 leading-snug m-0">
            Set <code class="text-blue-300 font-mono text-[10px]">startLocation = "$baseURL/users/sign_in"</code> for mobile auth entry.
          </p>
        </div>
      </div>

      <!-- Right Column: Real MainActivity.kt Code Snippet (Cols 6-12) -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
          <span class="text-emerald-400 font-bold">android/app/src/main/java/et/netale/litloop/MainActivity.kt</span>
          <span class="bg-slate-900 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold">LitLoop Kotlin</span>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed">
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

    <!-- Bottom Takeaway Banner -->
    <div class="mt-3 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs">
      <span class="text-slate-300">
        ⚡ <strong>LitLoop Android Setup:</strong> Kotlin <code class="text-emerald-300">MainActivity</code> points navigator directly to <code class="text-emerald-300">https://litloop.club/users/sign_in</code>.
      </span>
      <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-700 shrink-0 font-bold ml-2">
        LitLoop Android 🤖
      </span>
    </div>

  </div>
</template>

<script setup>
</script>
