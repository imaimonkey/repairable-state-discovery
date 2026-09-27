# V2R cluster inventory

2026-09-27T14:57:45.609989+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748085248 available bytes; 83.00% used; 112401393 free inodes.

server1 `/home`: 304748085248 available bytes; 83.00% used; 112401393 free inodes.

server1 `/tmp`: 304748085248 available bytes; 83.00% used; 112401393 free inodes.

server1 `/var/tmp`: 304748085248 available bytes; 83.00% used; 112401393 free inodes.

server1 `/mnt/raid5`: 630116196352 available bytes; 97.11% used; 337424040 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 13413421056 available bytes; 99.25% used; 110351801 free inodes.

server2 `/home`: 13413421056 available bytes; 99.25% used; 110351801 free inodes.

server2 `/tmp`: 13413421056 available bytes; 99.25% used; 110351801 free inodes.

server2 `/var/tmp`: 13413421056 available bytes; 99.25% used; 110351801 free inodes.

server2 `/mnt/raid5`: 525250936832 available bytes; 96.37% used; 444721688 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78558121984 available bytes; 95.62% used; 114062771 free inodes.

server3 `/home`: 78558121984 available bytes; 95.62% used; 114062771 free inodes.

server3 `/data`: 1328691806208 available bytes; 81.64% used; 225756522 free inodes.

server3 `/tmp`: 78558121984 available bytes; 95.62% used; 114062771 free inodes.

server3 `/var/tmp`: 78558121984 available bytes; 95.62% used; 114062771 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109349076992 available bytes; 93.90% used; 114372743 free inodes.

server4 `/home`: 109349076992 available bytes; 93.90% used; 114372743 free inodes.

server4 `/data`: 350416146432 available bytes; 95.16% used; 224727241 free inodes.

server4 `/tmp`: 109349076992 available bytes; 93.90% used; 114372743 free inodes.

server4 `/var/tmp`: 109349076992 available bytes; 93.90% used; 114372743 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
