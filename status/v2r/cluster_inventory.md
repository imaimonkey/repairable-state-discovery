# V2R cluster inventory

2026-09-24T06:25:47.365027+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324511199232 available bytes; 81.90% used; 112491707 free inodes.

server1 `/home`: 324511199232 available bytes; 81.90% used; 112491707 free inodes.

server1 `/tmp`: 324511199232 available bytes; 81.90% used; 112491707 free inodes.

server1 `/var/tmp`: 324511199232 available bytes; 81.90% used; 112491707 free inodes.

server1 `/mnt/raid5`: 517575106560 available bytes; 97.63% used; 337723765 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57882959872 available bytes; 96.77% used; 110431217 free inodes.

server2 `/home`: 57882959872 available bytes; 96.77% used; 110431217 free inodes.

server2 `/tmp`: 57882959872 available bytes; 96.77% used; 110431217 free inodes.

server2 `/var/tmp`: 57882959872 available bytes; 96.77% used; 110431217 free inodes.

server2 `/mnt/raid5`: 520392040448 available bytes; 96.40% used; 445192168 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127211192320 available bytes; 92.90% used; 114199768 free inodes.

server3 `/home`: 127211192320 available bytes; 92.90% used; 114199768 free inodes.

server3 `/data`: 140550320128 available bytes; 98.06% used; 225835845 free inodes.

server3 `/tmp`: 127211192320 available bytes; 92.90% used; 114199768 free inodes.

server3 `/var/tmp`: 127211192320 available bytes; 92.90% used; 114199768 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805668352 available bytes; 94.10% used; 114349280 free inodes.

server4 `/home`: 105805668352 available bytes; 94.10% used; 114349280 free inodes.

server4 `/data`: 331429007360 available bytes; 95.42% used; 225373188 free inodes.

server4 `/tmp`: 105805668352 available bytes; 94.10% used; 114349280 free inodes.

server4 `/var/tmp`: 105805668352 available bytes; 94.10% used; 114349280 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
