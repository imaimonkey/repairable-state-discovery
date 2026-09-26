# V2R cluster inventory

2026-09-26T00:16:01.504473+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318669041664 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318669041664 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318669041664 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318669041664 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 359563255808 available bytes; 98.35% used; 337547052 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22947729408 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22947729408 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22947729408 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22947729408 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 296026259456 available bytes; 97.95% used; 445058492 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341317632 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84341317632 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124945625088 available bytes; 98.27% used; 225819292 free inodes.

server3 `/tmp`: 84341317632 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84341317632 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453682688 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453682688 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178048622592 available bytes; 97.54% used; 224917551 free inodes.

server4 `/tmp`: 105453682688 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453682688 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
