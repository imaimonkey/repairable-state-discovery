# V2R cluster inventory

2026-09-24T12:06:46.722737+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324268105728 available bytes; 81.91% used; 112488316 free inodes.

server1 `/home`: 324268105728 available bytes; 81.91% used; 112488316 free inodes.

server1 `/tmp`: 324268105728 available bytes; 81.91% used; 112488316 free inodes.

server1 `/var/tmp`: 324268105728 available bytes; 81.91% used; 112488316 free inodes.

server1 `/mnt/raid5`: 405262282752 available bytes; 98.14% used; 337685129 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57623801856 available bytes; 96.79% used; 110429636 free inodes.

server2 `/home`: 57623801856 available bytes; 96.79% used; 110429636 free inodes.

server2 `/tmp`: 57623801856 available bytes; 96.79% used; 110429636 free inodes.

server2 `/var/tmp`: 57623801856 available bytes; 96.79% used; 110429636 free inodes.

server2 `/mnt/raid5`: 509219586048 available bytes; 96.48% used; 445172611 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85325238272 available bytes; 95.24% used; 114172841 free inodes.

server3 `/home`: 85325238272 available bytes; 95.24% used; 114172841 free inodes.

server3 `/data`: 163541057536 available bytes; 97.74% used; 225815563 free inodes.

server3 `/tmp`: 85325238272 available bytes; 95.24% used; 114172841 free inodes.

server3 `/var/tmp`: 85325238272 available bytes; 95.24% used; 114172841 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105718427648 available bytes; 94.10% used; 114348821 free inodes.

server4 `/home`: 105718427648 available bytes; 94.10% used; 114348821 free inodes.

server4 `/data`: 90433126400 available bytes; 98.75% used; 225257322 free inodes.

server4 `/tmp`: 105718427648 available bytes; 94.10% used; 114348821 free inodes.

server4 `/var/tmp`: 105718427648 available bytes; 94.10% used; 114348821 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
