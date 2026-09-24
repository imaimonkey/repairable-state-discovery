# V2R cluster inventory

2026-09-24T01:21:30.467371+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325469970432 available bytes; 81.84% used; 112499791 free inodes.

server1 `/home`: 325469970432 available bytes; 81.84% used; 112499791 free inodes.

server1 `/tmp`: 325469970432 available bytes; 81.84% used; 112499791 free inodes.

server1 `/var/tmp`: 325469970432 available bytes; 81.84% used; 112499791 free inodes.

server1 `/mnt/raid5`: 932835180544 available bytes; 95.72% used; 337734035 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40953503744 available bytes; 97.72% used; 110432061 free inodes.

server2 `/home`: 40953503744 available bytes; 97.72% used; 110432061 free inodes.

server2 `/tmp`: 40953503744 available bytes; 97.72% used; 110432061 free inodes.

server2 `/var/tmp`: 40953503744 available bytes; 97.72% used; 110432061 free inodes.

server2 `/mnt/raid5`: 531223117824 available bytes; 96.33% used; 445201994 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292346847232 available bytes; 83.69% used; 114187474 free inodes.

server3 `/home`: 292346847232 available bytes; 83.69% used; 114187474 free inodes.

server3 `/data`: 82051375104 available bytes; 98.87% used; 225842449 free inodes.

server3 `/tmp`: 292346847232 available bytes; 83.69% used; 114187474 free inodes.

server3 `/var/tmp`: 292346847232 available bytes; 83.69% used; 114187474 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105977217024 available bytes; 94.09% used; 114348984 free inodes.

server4 `/home`: 105977217024 available bytes; 94.09% used; 114348984 free inodes.

server4 `/data`: 290841001984 available bytes; 95.98% used; 225397003 free inodes.

server4 `/tmp`: 105977217024 available bytes; 94.09% used; 114348984 free inodes.

server4 `/var/tmp`: 105977217024 available bytes; 94.09% used; 114348984 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
