# V2R cluster inventory

2026-09-27T02:57:44.017253+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315081560064 available bytes; 82.42% used; 112443056 free inodes.

server1 `/home`: 315081560064 available bytes; 82.42% used; 112443056 free inodes.

server1 `/tmp`: 315081560064 available bytes; 82.42% used; 112443056 free inodes.

server1 `/var/tmp`: 315081560064 available bytes; 82.42% used; 112443056 free inodes.

server1 `/mnt/raid5`: 636813258752 available bytes; 97.08% used; 337401394 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17634217984 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17634217984 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17634217984 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17634217984 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 579657748480 available bytes; 95.99% used; 444883936 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78706311168 available bytes; 95.61% used; 114062942 free inodes.

server3 `/home`: 78706311168 available bytes; 95.61% used; 114062942 free inodes.

server3 `/data`: 1336574529536 available bytes; 81.53% used; 225761869 free inodes.

server3 `/tmp`: 78706311168 available bytes; 95.61% used; 114062942 free inodes.

server3 `/var/tmp`: 78706311168 available bytes; 95.61% used; 114062942 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111035551744 available bytes; 93.80% used; 114373230 free inodes.

server4 `/home`: 111035551744 available bytes; 93.80% used; 114373230 free inodes.

server4 `/data`: 396888801280 available bytes; 94.51% used; 224781277 free inodes.

server4 `/tmp`: 111035551744 available bytes; 93.80% used; 114373230 free inodes.

server4 `/var/tmp`: 111035551744 available bytes; 93.80% used; 114373230 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
