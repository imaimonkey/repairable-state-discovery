# V2R cluster inventory

2026-09-25T02:17:39.197317+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318970310656 available bytes; 82.21% used; 112480554 free inodes.

server1 `/home`: 318970310656 available bytes; 82.21% used; 112480554 free inodes.

server1 `/tmp`: 318970310656 available bytes; 82.21% used; 112480554 free inodes.

server1 `/var/tmp`: 318970310656 available bytes; 82.21% used; 112480554 free inodes.

server1 `/mnt/raid5`: 416238641152 available bytes; 98.09% used; 337607389 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23016210432 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23016210432 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23016210432 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23016210432 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 483789647872 available bytes; 96.66% used; 445114116 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145797980160 available bytes; 97.99% used; 225811330 free inodes.

server3 `/tmp`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84350377984 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105752248320 available bytes; 94.10% used; 114348235 free inodes.

server4 `/home`: 105752248320 available bytes; 94.10% used; 114348235 free inodes.

server4 `/data`: 38282190848 available bytes; 99.47% used; 224970359 free inodes.

server4 `/tmp`: 105752248320 available bytes; 94.10% used; 114348235 free inodes.

server4 `/var/tmp`: 105752248320 available bytes; 94.10% used; 114348235 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
