# V2R cluster inventory

2026-09-24T01:01:20.725247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325524611072 available bytes; 81.84% used; 112500259 free inodes.

server1 `/home`: 325524611072 available bytes; 81.84% used; 112500259 free inodes.

server1 `/tmp`: 325524611072 available bytes; 81.84% used; 112500259 free inodes.

server1 `/var/tmp`: 325524611072 available bytes; 81.84% used; 112500259 free inodes.

server1 `/mnt/raid5`: 1014869344256 available bytes; 95.34% used; 337734903 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40970682368 available bytes; 97.71% used; 110432209 free inodes.

server2 `/home`: 40970682368 available bytes; 97.71% used; 110432209 free inodes.

server2 `/tmp`: 40970682368 available bytes; 97.71% used; 110432209 free inodes.

server2 `/var/tmp`: 40970682368 available bytes; 97.71% used; 110432209 free inodes.

server2 `/mnt/raid5`: 531821727744 available bytes; 96.33% used; 445202488 free inodes.
| server3 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292744491008 available bytes; 83.66% used; 114211798 free inodes.

server3 `/home`: 292744491008 available bytes; 83.66% used; 114211798 free inodes.

server3 `/data`: 82088402944 available bytes; 98.87% used; 225843239 free inodes.

server3 `/tmp`: 292744491008 available bytes; 83.66% used; 114211798 free inodes.

server3 `/var/tmp`: 292744491008 available bytes; 83.66% used; 114211798 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106018676736 available bytes; 94.08% used; 114349517 free inodes.

server4 `/home`: 106018676736 available bytes; 94.08% used; 114349517 free inodes.

server4 `/data`: 292874842112 available bytes; 95.95% used; 225414559 free inodes.

server4 `/tmp`: 106018676736 available bytes; 94.08% used; 114349517 free inodes.

server4 `/var/tmp`: 106018676736 available bytes; 94.08% used; 114349517 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
