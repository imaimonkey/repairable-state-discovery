# V2R cluster inventory

2026-09-25T19:18:29.825554+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318735544320 available bytes; 82.22% used; 112476343 free inodes.

server1 `/home`: 318735544320 available bytes; 82.22% used; 112476343 free inodes.

server1 `/tmp`: 318735544320 available bytes; 82.22% used; 112476343 free inodes.

server1 `/var/tmp`: 318735544320 available bytes; 82.22% used; 112476343 free inodes.

server1 `/mnt/raid5`: 370882064384 available bytes; 98.30% used; 337540844 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23101345792 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23101345792 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23101345792 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23101345792 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 312408174592 available bytes; 97.84% used; 445064791 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382486528 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84382486528 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 129285894144 available bytes; 98.21% used; 225808781 free inodes.

server3 `/tmp`: 84382486528 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84382486528 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675141120 available bytes; 94.10% used; 114349589 free inodes.

server4 `/home`: 105675141120 available bytes; 94.10% used; 114349589 free inodes.

server4 `/data`: 229637591040 available bytes; 96.83% used; 224930598 free inodes.

server4 `/tmp`: 105675141120 available bytes; 94.10% used; 114349589 free inodes.

server4 `/var/tmp`: 105675141120 available bytes; 94.10% used; 114349589 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
