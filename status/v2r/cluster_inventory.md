# V2R cluster inventory

2026-09-25T20:54:48.561152+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318699061248 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318699061248 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318699061248 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318699061248 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 368625172480 available bytes; 98.31% used; 337539544 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22894952448 available bytes; 98.72% used; 110405678 free inodes.

server2 `/home`: 22894952448 available bytes; 98.72% used; 110405678 free inodes.

server2 `/tmp`: 22894952448 available bytes; 98.72% used; 110405678 free inodes.

server2 `/var/tmp`: 22894952448 available bytes; 98.72% used; 110405678 free inodes.

server2 `/mnt/raid5`: 302579097600 available bytes; 97.91% used; 445056482 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84362485760 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84362485760 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127100989440 available bytes; 98.24% used; 225807633 free inodes.

server3 `/tmp`: 84362485760 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84362485760 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655304192 available bytes; 94.10% used; 114349534 free inodes.

server4 `/home`: 105655304192 available bytes; 94.10% used; 114349534 free inodes.

server4 `/data`: 228019290112 available bytes; 96.85% used; 224926773 free inodes.

server4 `/tmp`: 105655304192 available bytes; 94.10% used; 114349534 free inodes.

server4 `/var/tmp`: 105655304192 available bytes; 94.10% used; 114349534 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
