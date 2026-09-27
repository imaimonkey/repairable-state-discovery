# V2R cluster inventory

2026-09-27T10:13:50.026142+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314436694016 available bytes; 82.46% used; 112440680 free inodes.

server1 `/home`: 314436694016 available bytes; 82.46% used; 112440680 free inodes.

server1 `/tmp`: 314436694016 available bytes; 82.46% used; 112440680 free inodes.

server1 `/var/tmp`: 314436694016 available bytes; 82.46% used; 112440680 free inodes.

server1 `/mnt/raid5`: 635420172288 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16505212928 available bytes; 99.08% used; 110356613 free inodes.

server2 `/home`: 16505212928 available bytes; 99.08% used; 110356613 free inodes.

server2 `/tmp`: 16505212928 available bytes; 99.08% used; 110356613 free inodes.

server2 `/var/tmp`: 16505212928 available bytes; 99.08% used; 110356613 free inodes.

server2 `/mnt/raid5`: 572260163584 available bytes; 96.05% used; 444739772 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78544740352 available bytes; 95.62% used; 114062830 free inodes.

server3 `/home`: 78544740352 available bytes; 95.62% used; 114062830 free inodes.

server3 `/data`: 1332212117504 available bytes; 81.59% used; 225761218 free inodes.

server3 `/tmp`: 78544740352 available bytes; 95.62% used; 114062830 free inodes.

server3 `/var/tmp`: 78544740352 available bytes; 95.62% used; 114062830 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111049134080 available bytes; 93.80% used; 114372831 free inodes.

server4 `/home`: 111049134080 available bytes; 93.80% used; 114372831 free inodes.

server4 `/data`: 363808088064 available bytes; 94.97% used; 224766943 free inodes.

server4 `/tmp`: 111049134080 available bytes; 93.80% used; 114372831 free inodes.

server4 `/var/tmp`: 111049134080 available bytes; 93.80% used; 114372831 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
