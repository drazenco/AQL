// sdk/js/index.js
// Placeholder for future JS SDK. Intentionally minimal for v0.1.
export function surface(query, opts = {}) {
  return fetch((opts.baseUrl || 'http://localhost:8000') + '/aql/surface', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, k: opts.k || 10, return_prob: !!opts.return_prob, lam: opts.lam || 10.0 }),
  }).then(r => r.json());
}
