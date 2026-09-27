# V2R cluster inventory

2026-09-27T07:24:56.935493+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314477662208 available bytes; 82.46% used; 112440786 free inodes.

server1 `/home`: 314477662208 available bytes; 82.46% used; 112440786 free inodes.

server1 `/tmp`: 314477662208 available bytes; 82.46% used; 112440786 free inodes.

server1 `/var/tmp`: 314477662208 available bytes; 82.46% used; 112440786 free inodes.

server1 `/mnt/raid5`: 634657112064 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 17609064448 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17609064448 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17609064448 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17609064448 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 571527135232 available bytes; 96.05% used; 444874181 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78578356224 available bytes; 95.62% used; 114062885 free inodes.

server3 `/home`: 78578356224 available bytes; 95.62% used; 114062885 free inodes.

server3 `/data`: 1333051113472 available bytes; 81.58% used; 225764176 free inodes.

server3 `/tmp`: 78578356224 available bytes; 95.62% used; 114062885 free inodes.

server3 `/var/tmp`: 78578356224 available bytes; 95.62% used; 114062885 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070683136 available bytes; 93.80% used; 114372905 free inodes.

server4 `/home`: 111070683136 available bytes; 93.80% used; 114372905 free inodes.

server4 `/data`: 374350053376 available bytes; 94.83% used; 224771151 free inodes.

server4 `/tmp`: 111070683136 available bytes; 93.80% used; 114372905 free inodes.

server4 `/var/tmp`: 111070683136 available bytes; 93.80% used; 114372905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
