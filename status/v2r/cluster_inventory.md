# V2R cluster inventory

2026-09-24T09:43:14.801569+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/home`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/tmp`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/var/tmp`: 324452655104 available bytes; 81.90% used; 112489727 free inodes.

server1 `/mnt/raid5`: 501801115648 available bytes; 97.70% used; 337711790 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/home`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/tmp`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/var/tmp`: 57764257792 available bytes; 96.78% used; 110430786 free inodes.

server2 `/mnt/raid5`: 514198597632 available bytes; 96.45% used; 445177125 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85833617408 available bytes; 95.21% used; 114199436 free inodes.

server3 `/home`: 85833617408 available bytes; 95.21% used; 114199436 free inodes.

server3 `/data`: 165688709120 available bytes; 97.71% used; 225819930 free inodes.

server3 `/tmp`: 85833617408 available bytes; 95.21% used; 114199436 free inodes.

server3 `/var/tmp`: 85833617408 available bytes; 95.21% used; 114199436 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748688896 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748688896 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154557452288 available bytes; 97.86% used; 225273206 free inodes.

server4 `/tmp`: 105748688896 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748688896 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
