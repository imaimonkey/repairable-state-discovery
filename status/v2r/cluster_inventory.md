# V2R cluster inventory

2026-09-24T11:48:02.881237+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324341227520 available bytes; 81.91% used; 112488802 free inodes.

server1 `/home`: 324341227520 available bytes; 81.91% used; 112488802 free inodes.

server1 `/tmp`: 324341227520 available bytes; 81.91% used; 112488802 free inodes.

server1 `/var/tmp`: 324341227520 available bytes; 81.91% used; 112488802 free inodes.

server1 `/mnt/raid5`: 424111038464 available bytes; 98.05% used; 337687205 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57642000384 available bytes; 96.78% used; 110429820 free inodes.

server2 `/home`: 57642000384 available bytes; 96.78% used; 110429820 free inodes.

server2 `/tmp`: 57642000384 available bytes; 96.78% used; 110429820 free inodes.

server2 `/var/tmp`: 57642000384 available bytes; 96.78% used; 110429820 free inodes.

server2 `/mnt/raid5`: 510079041536 available bytes; 96.48% used; 445172699 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85246631936 available bytes; 95.24% used; 114166874 free inodes.

server3 `/home`: 85246631936 available bytes; 95.24% used; 114166874 free inodes.

server3 `/data`: 163668361216 available bytes; 97.74% used; 225815897 free inodes.

server3 `/tmp`: 85246631936 available bytes; 95.24% used; 114166874 free inodes.

server3 `/var/tmp`: 85246631936 available bytes; 95.24% used; 114166874 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727623168 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727623168 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115387113472 available bytes; 98.41% used; 225257947 free inodes.

server4 `/tmp`: 105727623168 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727623168 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
