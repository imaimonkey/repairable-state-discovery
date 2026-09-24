# V2R cluster inventory

2026-09-24T09:57:13.186636+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324431032320 available bytes; 81.90% used; 112489549 free inodes.

server1 `/home`: 324431032320 available bytes; 81.90% used; 112489549 free inodes.

server1 `/tmp`: 324431032320 available bytes; 81.90% used; 112489549 free inodes.

server1 `/var/tmp`: 324431032320 available bytes; 81.90% used; 112489549 free inodes.

server1 `/mnt/raid5`: 500715491328 available bytes; 97.70% used; 337701713 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57754845184 available bytes; 96.78% used; 110430745 free inodes.

server2 `/home`: 57754845184 available bytes; 96.78% used; 110430745 free inodes.

server2 `/tmp`: 57754845184 available bytes; 96.78% used; 110430745 free inodes.

server2 `/var/tmp`: 57754845184 available bytes; 96.78% used; 110430745 free inodes.

server2 `/mnt/raid5`: 513786122240 available bytes; 96.45% used; 445177076 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85799948288 available bytes; 95.21% used; 114198717 free inodes.

server3 `/home`: 85799948288 available bytes; 95.21% used; 114198717 free inodes.

server3 `/data`: 165581598720 available bytes; 97.71% used; 225819670 free inodes.

server3 `/tmp`: 85799948288 available bytes; 95.21% used; 114198717 free inodes.

server3 `/var/tmp`: 85799948288 available bytes; 95.21% used; 114198717 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748189184 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748189184 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154558701568 available bytes; 97.86% used; 225273206 free inodes.

server4 `/tmp`: 105748189184 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748189184 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
