# V2R cluster inventory

2026-09-26T01:27:43.764574+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318649729024 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318649729024 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318649729024 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318649729024 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345501077504 available bytes; 98.42% used; 337546557 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22928498688 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22928498688 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22928498688 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22928498688 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 290798161920 available bytes; 97.99% used; 445056054 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84336308224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84336308224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124866052096 available bytes; 98.27% used; 225818072 free inodes.

server3 `/tmp`: 84336308224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84336308224 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105264205824 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264205824 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141688291328 available bytes; 98.04% used; 224917299 free inodes.

server4 `/tmp`: 105264205824 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264205824 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
