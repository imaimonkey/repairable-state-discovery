# V2R cluster inventory

2026-09-23T21:11:42.527969+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325718196224 available bytes; 81.83% used; 112501445 free inodes.

server1 `/home`: 325718196224 available bytes; 81.83% used; 112501445 free inodes.

server1 `/tmp`: 325718196224 available bytes; 81.83% used; 112501445 free inodes.

server1 `/var/tmp`: 325718196224 available bytes; 81.83% used; 112501445 free inodes.

server1 `/mnt/raid5`: 1388134125568 available bytes; 93.63% used; 337739978 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41119645696 available bytes; 97.71% used; 110432705 free inodes.

server2 `/home`: 41119645696 available bytes; 97.71% used; 110432705 free inodes.

server2 `/tmp`: 41119645696 available bytes; 97.71% used; 110432705 free inodes.

server2 `/var/tmp`: 41119645696 available bytes; 97.71% used; 110432705 free inodes.

server2 `/mnt/raid5`: 539087814656 available bytes; 96.28% used; 445209408 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293464854528 available bytes; 83.62% used; 114236284 free inodes.

server3 `/home`: 293464854528 available bytes; 83.62% used; 114236284 free inodes.

server3 `/data`: 52310786048 available bytes; 99.28% used; 225849507 free inodes.

server3 `/tmp`: 293464854528 available bytes; 83.62% used; 114236284 free inodes.

server3 `/var/tmp`: 293464854528 available bytes; 83.62% used; 114236284 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106493018112 available bytes; 94.06% used; 114356041 free inodes.

server4 `/home`: 106493018112 available bytes; 94.06% used; 114356041 free inodes.

server4 `/data`: 300475420672 available bytes; 95.85% used; 225454670 free inodes.

server4 `/tmp`: 106493018112 available bytes; 94.06% used; 114356041 free inodes.

server4 `/var/tmp`: 106493018112 available bytes; 94.06% used; 114356041 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
