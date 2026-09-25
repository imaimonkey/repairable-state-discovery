# V2R cluster inventory

2026-09-25T22:16:59.475653+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318694182912 available bytes; 82.22% used; 112476304 free inodes.

server1 `/home`: 318694182912 available bytes; 82.22% used; 112476304 free inodes.

server1 `/tmp`: 318694182912 available bytes; 82.22% used; 112476304 free inodes.

server1 `/var/tmp`: 318694182912 available bytes; 82.22% used; 112476304 free inodes.

server1 `/mnt/raid5`: 360267194368 available bytes; 98.35% used; 337539002 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22947057664 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22947057664 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22947057664 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22947057664 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 299347886080 available bytes; 97.93% used; 445053340 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84357283840 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84357283840 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125872500736 available bytes; 98.26% used; 225806206 free inodes.

server3 `/tmp`: 84357283840 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84357283840 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105312038912 available bytes; 94.12% used; 114347143 free inodes.

server4 `/home`: 105312038912 available bytes; 94.12% used; 114347143 free inodes.

server4 `/data`: 207174119424 available bytes; 97.14% used; 224917928 free inodes.

server4 `/tmp`: 105312038912 available bytes; 94.12% used; 114347143 free inodes.

server4 `/var/tmp`: 105312038912 available bytes; 94.12% used; 114347143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
