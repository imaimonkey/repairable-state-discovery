# V2R cluster inventory

2026-09-27T04:01:46.041923+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315076026368 available bytes; 82.42% used; 112443048 free inodes.

server1 `/home`: 315076026368 available bytes; 82.42% used; 112443048 free inodes.

server1 `/tmp`: 315076026368 available bytes; 82.42% used; 112443048 free inodes.

server1 `/var/tmp`: 315076026368 available bytes; 82.42% used; 112443048 free inodes.

server1 `/mnt/raid5`: 636759015424 available bytes; 97.08% used; 337401271 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17633488896 available bytes; 99.02% used; 110365009 free inodes.

server2 `/home`: 17633488896 available bytes; 99.02% used; 110365009 free inodes.

server2 `/tmp`: 17633488896 available bytes; 99.02% used; 110365009 free inodes.

server2 `/var/tmp`: 17633488896 available bytes; 99.02% used; 110365009 free inodes.

server2 `/mnt/raid5`: 577771966464 available bytes; 96.01% used; 444882700 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78696103936 available bytes; 95.61% used; 114062926 free inodes.

server3 `/home`: 78696103936 available bytes; 95.61% used; 114062926 free inodes.

server3 `/data`: 1335188189184 available bytes; 81.55% used; 225759695 free inodes.

server3 `/tmp`: 78696103936 available bytes; 95.61% used; 114062926 free inodes.

server3 `/var/tmp`: 78696103936 available bytes; 95.61% used; 114062926 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111018831872 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111018831872 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382183239680 available bytes; 94.72% used; 224780779 free inodes.

server4 `/tmp`: 111018831872 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111018831872 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
