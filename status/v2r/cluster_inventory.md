# V2R cluster inventory

2026-09-26T01:24:40.561116+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318648995840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318648995840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318648995840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318648995840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345508061184 available bytes; 98.42% used; 337546577 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929776640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22929776640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22929776640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22929776640 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 290881687552 available bytes; 97.99% used; 445056070 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339326976 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84339326976 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124869087232 available bytes; 98.27% used; 225818123 free inodes.

server3 `/tmp`: 84339326976 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84339326976 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105264291840 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264291840 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141689282560 available bytes; 98.04% used; 224917305 free inodes.

server4 `/tmp`: 105264291840 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264291840 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
