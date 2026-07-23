<template>
  <div class="comparison-matrix my-3 overflow-hidden rounded-xl border border-slate-800 bg-slate-950/80 shadow-2xl text-left">
    <table class="w-full text-xs text-slate-300 border-collapse">
      <thead>
        <tr class="bg-slate-900 border-b border-slate-800 text-slate-200 uppercase font-mono text-[11px]">
          <th class="p-3 text-left">Metric / Capability</th>
          <th class="p-3 text-center bg-slate-900/60 text-slate-400">React Native / Flutter</th>
          <th class="p-3 text-center bg-red-950/60 text-red-300 border-l border-r border-red-500/30">
            🔥 Rails + Hotwire Native
          </th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 font-sans">
        <tr>
          <td class="p-3 font-semibold text-white">Time-To-Market (MVP to Prod)</td>
          <td class="p-3 text-center text-slate-400">8–12 Weeks (dual dev cycles)</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            1–2 Weeks ⚡ (80% faster delivery)
          </td>
        </tr>
        <tr>
          <td class="p-3 font-semibold text-white">Engineering Headcount Needed</td>
          <td class="p-3 text-center text-slate-400">4–6 Devs (Web + iOS + Android + API)</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            1–2 Full-Stack Rails Engineers 🚀
          </td>
        </tr>
        <tr>
          <td class="p-3 font-semibold text-white">Feature Release Cycle</td>
          <td class="p-3 text-center text-slate-400">App Store review queues (2–5 days)</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            Instant! Push to Rails server ✨
          </td>
        </tr>
        <tr>
          <td class="p-3 font-semibold text-white">Native Navigation & UX</td>
          <td class="p-3 text-center text-slate-400">Emulated JS navigation transitions</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            100% Real iOS & Android Controllers
          </td>
        </tr>
        <tr>
          <td class="p-3 font-semibold text-white">Native Hardware Access</td>
          <td class="p-3 text-center text-slate-400">NPM bridge wrappers & native plugins</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            Strada Web-to-Native Components
          </td>
        </tr>
        <tr>
          <td class="p-3 font-semibold text-white">Business Logic Duplication</td>
          <td class="p-3 text-center text-slate-400">High (duplicated validation & state)</td>
          <td class="p-3 text-center font-bold text-emerald-400 bg-red-950/20 border-l border-r border-red-500/20">
            Zero! Single source of truth in Rails
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
</script>
