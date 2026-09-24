# V2R cluster inventory

2026-09-24T10:20:32.190105+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324417519616 available bytes; 81.90% used; 112489355 free inodes.

server1 `/home`: 324417519616 available bytes; 81.90% used; 112489355 free inodes.

server1 `/tmp`: 324417519616 available bytes; 81.90% used; 112489355 free inodes.

server1 `/var/tmp`: 324417519616 available bytes; 81.90% used; 112489355 free inodes.

server1 `/mnt/raid5`: 500634333184 available bytes; 97.70% used; 337698960 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57736359936 available bytes; 96.78% used; 110430685 free inodes.

server2 `/home`: 57736359936 available bytes; 96.78% used; 110430685 free inodes.

server2 `/tmp`: 57736359936 available bytes; 96.78% used; 110430685 free inodes.

server2 `/var/tmp`: 57736359936 available bytes; 96.78% used; 110430685 free inodes.

server2 `/mnt/raid5`: 513017876480 available bytes; 96.46% used; 445175557 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85831229440 available bytes; 95.21% used; 114199277 free inodes.

server3 `/home`: 85831229440 available bytes; 95.21% used; 114199277 free inodes.

server3 `/data`: 164370411520 available bytes; 97.73% used; 225818814 free inodes.

server3 `/tmp`: 85831229440 available bytes; 95.21% used; 114199277 free inodes.

server3 `/var/tmp`: 85831229440 available bytes; 95.21% used; 114199277 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747046400 available bytes; 94.10% used; 114348987 free inodes.

server4 `/home`: 105747046400 available bytes; 94.10% used; 114348987 free inodes.

server4 `/data`: 153481814016 available bytes; 97.88% used; 225258417 free inodes.

server4 `/tmp`: 105747046400 available bytes; 94.10% used; 114348987 free inodes.

server4 `/var/tmp`: 105747046400 available bytes; 94.10% used; 114348987 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
