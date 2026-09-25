# V2R cluster inventory

2026-09-25T18:55:20.200053+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318740176896 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318740176896 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318740176896 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318740176896 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 371040702464 available bytes; 98.30% used; 337541086 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23097118720 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23097118720 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23097118720 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23097118720 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 313234681856 available bytes; 97.84% used; 445065790 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84383207424 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84383207424 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131373346816 available bytes; 98.18% used; 225809223 free inodes.

server3 `/tmp`: 84383207424 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84383207424 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105606729728 available bytes; 94.11% used; 114349597 free inodes.

server4 `/home`: 105606729728 available bytes; 94.11% used; 114349597 free inodes.

server4 `/data`: 229687795712 available bytes; 96.83% used; 224931391 free inodes.

server4 `/tmp`: 105606729728 available bytes; 94.11% used; 114349597 free inodes.

server4 `/var/tmp`: 105606729728 available bytes; 94.11% used; 114349597 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
