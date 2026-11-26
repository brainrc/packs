---
name: brainrc-node-ts
description: Node.js and TypeScript projects. Type-check with tsc, lint with ESLint and typescript-eslint, run the package's tests, and a review checklist. Use when writing, changing, or reviewing *.ts, *.tsx, *.js, *.mjs files, package.json, or tsconfig*.json.
---

# brainrc-node-ts

## Validate (offline)
Use the package manager the lock file names: `pnpm-lock.yaml` → pnpm, `yarn.lock` → yarn,
`bun.lock`/`bun.lockb` → bun, otherwise npm. Prefer the project's own scripts.
```bash
<pm> run typecheck            # if defined; else npx tsc --noEmit (-p <tsconfig> in a monorepo)
<pm> run lint                 # if defined; else npx eslint .  (flat config: eslint.config.*)
<pm> test                     # the package's test script
<pm> run build                # if the change touches build output or exports
```
In a workspace, scope each command to the changed packages (`pnpm --filter <pkg>`,
`npm -w <pkg>`).

## Conventions
- ESLint uses the flat config (`eslint.config.mjs`); typescript-eslint's
  `tseslint.configs.recommended` is the baseline. Don't add a second lint or format config.
- Keep `strict` on in `tsconfig.json`; no `any` where a real type or `unknown` fits.
- Match the package's module system (`"type": "module"` or CommonJS) and import style.
- Dependencies go in `package.json` through the package manager, which updates the lock file;
  never hand-edit a lock file. Runtime code goes in `dependencies`, tools in `devDependencies`.
- Async code awaits or returns every promise; no floating promises.

## Review checklist
- [ ] Type-check, lint and tests pass for the changed packages.
- [ ] No new `any`, `@ts-ignore` or `eslint-disable` without a reason next to it.
- [ ] Errors are handled or rethrown with context; no empty `catch`.
- [ ] Public API changes (exports, types) are intended and noted for the changelog.
- [ ] No secrets in code, `.env` files or test fixtures.

## Never without approval
- Install, upgrade or remove dependencies (`npm install <pkg>`, `pnpm add`, `npx` of a package the
  project doesn't list): name what you'd install and ask.
- Delete and regenerate a lock file, or run an audit fix that rewrites it.
- Publish (`npm publish`) or change the package's version.
