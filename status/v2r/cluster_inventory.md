# V2R cluster inventory

2026-09-24T17:05:49.234932+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324021886976 available bytes; 81.92% used; 112481436 free inodes.

server1 `/home`: 324021886976 available bytes; 81.92% used; 112481436 free inodes.

server1 `/tmp`: 324021886976 available bytes; 81.92% used; 112481436 free inodes.

server1 `/var/tmp`: 324021886976 available bytes; 81.92% used; 112481436 free inodes.

server1 `/mnt/raid5`: 416504963072 available bytes; 98.09% used; 337649211 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57062215680 available bytes; 96.82% used; 110417952 free inodes.

server2 `/home`: 57062215680 available bytes; 96.82% used; 110417952 free inodes.

server2 `/tmp`: 57062215680 available bytes; 96.82% used; 110417952 free inodes.

server2 `/var/tmp`: 57062215680 available bytes; 96.82% used; 110417952 free inodes.

server2 `/mnt/raid5`: 499836641280 available bytes; 96.55% used; 445163325 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417855488 available bytes; 95.29% used; 114156152 free inodes.

server3 `/home`: 84417855488 available bytes; 95.29% used; 114156152 free inodes.

server3 `/data`: 159106342912 available bytes; 97.80% used; 225787302 free inodes.

server3 `/tmp`: 84417855488 available bytes; 95.29% used; 114156152 free inodes.

server3 `/var/tmp`: 84417855488 available bytes; 95.29% used; 114156152 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682280448 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105682280448 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89166696448 available bytes; 98.77% used; 225254808 free inodes.

server4 `/tmp`: 105682280448 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105682280448 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
