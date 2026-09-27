# V2R cluster inventory

2026-09-27T04:59:41.845183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314800926720 available bytes; 82.44% used; 112443001 free inodes.

server1 `/home`: 314800926720 available bytes; 82.44% used; 112443001 free inodes.

server1 `/tmp`: 314800926720 available bytes; 82.44% used; 112443001 free inodes.

server1 `/var/tmp`: 314800926720 available bytes; 82.44% used; 112443001 free inodes.

server1 `/mnt/raid5`: 636044046336 available bytes; 97.08% used; 337400287 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17620803584 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17620803584 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17620803584 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17620803584 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 575970508800 available bytes; 96.02% used; 444878281 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78611996672 available bytes; 95.61% used; 114062917 free inodes.

server3 `/home`: 78611996672 available bytes; 95.61% used; 114062917 free inodes.

server3 `/data`: 1333646311424 available bytes; 81.57% used; 225758344 free inodes.

server3 `/tmp`: 78611996672 available bytes; 95.61% used; 114062917 free inodes.

server3 `/var/tmp`: 78611996672 available bytes; 95.61% used; 114062917 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111000555520 available bytes; 93.81% used; 114372922 free inodes.

server4 `/home`: 111000555520 available bytes; 93.81% used; 114372922 free inodes.

server4 `/data`: 382078181376 available bytes; 94.72% used; 224778237 free inodes.

server4 `/tmp`: 111000555520 available bytes; 93.81% used; 114372922 free inodes.

server4 `/var/tmp`: 111000555520 available bytes; 93.81% used; 114372922 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
