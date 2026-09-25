# V2R cluster inventory

2026-09-25T20:48:41.794034+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318700138496 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318700138496 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318700138496 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318700138496 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 368636616704 available bytes; 98.31% used; 337539567 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22896701440 available bytes; 98.72% used; 110405687 free inodes.

server2 `/home`: 22896701440 available bytes; 98.72% used; 110405687 free inodes.

server2 `/tmp`: 22896701440 available bytes; 98.72% used; 110405687 free inodes.

server2 `/var/tmp`: 22896701440 available bytes; 98.72% used; 110405687 free inodes.

server2 `/mnt/raid5`: 302756012032 available bytes; 97.91% used; 445056695 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371722240 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84371722240 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127102480384 available bytes; 98.24% used; 225807732 free inodes.

server3 `/tmp`: 84371722240 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84371722240 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655504896 available bytes; 94.10% used; 114349535 free inodes.

server4 `/home`: 105655504896 available bytes; 94.10% used; 114349535 free inodes.

server4 `/data`: 228023402496 available bytes; 96.85% used; 224926826 free inodes.

server4 `/tmp`: 105655504896 available bytes; 94.10% used; 114349535 free inodes.

server4 `/var/tmp`: 105655504896 available bytes; 94.10% used; 114349535 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
