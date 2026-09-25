# V2R cluster inventory

2026-09-25T19:21:33.218113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318735687680 available bytes; 82.22% used; 112476343 free inodes.

server1 `/home`: 318735687680 available bytes; 82.22% used; 112476343 free inodes.

server1 `/tmp`: 318735687680 available bytes; 82.22% used; 112476343 free inodes.

server1 `/var/tmp`: 318735687680 available bytes; 82.22% used; 112476343 free inodes.

server1 `/mnt/raid5`: 362751016960 available bytes; 98.34% used; 337540828 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095590912 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23095590912 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23095590912 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23095590912 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311784767488 available bytes; 97.85% used; 445064679 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382285824 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382285824 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 129286742016 available bytes; 98.21% used; 225808735 free inodes.

server3 `/tmp`: 84382285824 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382285824 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675055104 available bytes; 94.10% used; 114349587 free inodes.

server4 `/home`: 105675055104 available bytes; 94.10% used; 114349587 free inodes.

server4 `/data`: 229637259264 available bytes; 96.83% used; 224930404 free inodes.

server4 `/tmp`: 105675055104 available bytes; 94.10% used; 114349587 free inodes.

server4 `/var/tmp`: 105675055104 available bytes; 94.10% used; 114349587 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
