# V2R cluster inventory

2026-09-25T15:04:35.418707+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319125979136 available bytes; 82.20% used; 112476957 free inodes.

server1 `/home`: 319125979136 available bytes; 82.20% used; 112476957 free inodes.

server1 `/tmp`: 319125979136 available bytes; 82.20% used; 112476957 free inodes.

server1 `/var/tmp`: 319125979136 available bytes; 82.20% used; 112476957 free inodes.

server1 `/mnt/raid5`: 364003168256 available bytes; 98.33% used; 337546126 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 19261210624 available bytes; 98.93% used; 110407883 free inodes.

server2 `/home`: 19261210624 available bytes; 98.93% used; 110407883 free inodes.

server2 `/tmp`: 19261210624 available bytes; 98.93% used; 110407883 free inodes.

server2 `/var/tmp`: 19261210624 available bytes; 98.93% used; 110407883 free inodes.

server2 `/mnt/raid5`: 320678305792 available bytes; 97.78% used; 445073660 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84425953280 available bytes; 95.29% used; 114153448 free inodes.

server3 `/home`: 84425953280 available bytes; 95.29% used; 114153448 free inodes.

server3 `/data`: 142187065344 available bytes; 98.03% used; 225808128 free inodes.

server3 `/tmp`: 84425953280 available bytes; 95.29% used; 114153448 free inodes.

server3 `/var/tmp`: 84425953280 available bytes; 95.29% used; 114153448 free inodes.
| server4 | True | ['2', '3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636556800 available bytes; 94.11% used; 114349705 free inodes.

server4 `/home`: 105636556800 available bytes; 94.11% used; 114349705 free inodes.

server4 `/data`: 231351242752 available bytes; 96.80% used; 224944922 free inodes.

server4 `/tmp`: 105636556800 available bytes; 94.11% used; 114349705 free inodes.

server4 `/var/tmp`: 105636556800 available bytes; 94.11% used; 114349705 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
