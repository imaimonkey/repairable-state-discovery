# V2R cluster inventory

2026-09-24T02:24:22.142261+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325391163392 available bytes; 81.85% used; 112498937 free inodes.

server1 `/home`: 325391163392 available bytes; 81.85% used; 112498937 free inodes.

server1 `/tmp`: 325391163392 available bytes; 81.85% used; 112498937 free inodes.

server1 `/var/tmp`: 325391163392 available bytes; 81.85% used; 112498937 free inodes.

server1 `/mnt/raid5`: 669741379584 available bytes; 96.93% used; 337733261 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40892489728 available bytes; 97.72% used; 110431580 free inodes.

server2 `/home`: 40892489728 available bytes; 97.72% used; 110431580 free inodes.

server2 `/tmp`: 40892489728 available bytes; 97.72% used; 110431580 free inodes.

server2 `/var/tmp`: 40892489728 available bytes; 97.72% used; 110431580 free inodes.

server2 `/mnt/raid5`: 529206816768 available bytes; 96.34% used; 445199850 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291858280448 available bytes; 83.71% used; 114163143 free inodes.

server3 `/home`: 291858280448 available bytes; 83.71% used; 114163143 free inodes.

server3 `/data`: 39768010752 available bytes; 99.45% used; 225846827 free inodes.

server3 `/tmp`: 291858280448 available bytes; 83.71% used; 114163143 free inodes.

server3 `/var/tmp`: 291858280448 available bytes; 83.71% used; 114163143 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106012381184 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012381184 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289738260480 available bytes; 96.00% used; 225387624 free inodes.

server4 `/tmp`: 106012381184 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012381184 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
